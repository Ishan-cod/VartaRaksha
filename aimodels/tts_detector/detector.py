import torch
import librosa
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor

# Load model and feature extractor
model_name = "garystafford/wav2vec2-deepfake-voice-detector"
model = AutoModelForAudioClassification.from_pretrained(model_name)
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)

# Move to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

def detect_deepfake(audio_path):
    # Load audio
    audio, sr = librosa.load(
        audio_path,
        sr=16000,
        mono=True
    )

    # Feature extraction
    inputs = feature_extractor(
        audio,
        sampling_rate=16000,
        return_tensors="pt",
        padding=True
    )

    # Move tensors to CPU/GPU
    inputs = {
        k: v.to(device)
        for k, v in inputs.items()
    }

    # Inference
    with torch.inference_mode():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1)

    # Probabilities
    prob_real = probs[0][0].item()
    prob_fake = probs[0][1].item()

    prediction = "fake" if prob_fake > 0.5 else "real"

    return {
        "prediction": prediction,
        "real_probability": prob_real,
        "fake_probability": prob_fake,
        "confidence": max(prob_real, prob_fake)
    }
