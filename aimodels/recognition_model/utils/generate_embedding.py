import torch
import torch.nn.functional as F
from speechbrain.inference.speaker import EncoderClassifier
from speechbrain.utils.fetching import LocalStrategy
import torchaudio
import torchcodec


classifier = EncoderClassifier.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec-ecapa-voxceleb",
    local_strategy=LocalStrategy.COPY
)

def get_embedding(audio_path: str):

    waveform, sample_rate = torchaudio.load(audio_path)

    # Stereo -> mono
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    # SpeechBrain model expects 16 kHz
    if sample_rate != 16000:
        waveform = torchaudio.functional.resample(
            waveform,
            sample_rate,
            16000
        )

    # encode_batch expects [batch, time]
    waveform = waveform.squeeze(0)

    embedding = classifier.encode_batch(waveform) # type: ignore[attr-defined]

    embedding = embedding.squeeze()

    embedding = F.normalize(
        embedding,
        p=2,
        dim=0
    )

    return embedding
