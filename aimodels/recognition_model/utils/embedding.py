### THIS FILE IS IN DEVELOPMENT. DO NOT USE THIS ####

from speechbrain.inference.speaker import EncoderClassifier
from speechbrain.utils.fetching import LocalStrategy

classifier = EncoderClassifier.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/ecapa",
    local_strategy=LocalStrategy.COPY
)


def get_embedding(audio_path: str):
    embedding = classifier.encode_batch(audio_path)
    return embedding.squeeze()


embedding = get_embedding(
    r"D:\Chrome Download\LJ001-0001.wav"
)

print(embedding)