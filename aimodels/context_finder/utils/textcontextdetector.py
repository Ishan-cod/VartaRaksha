import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from aimodels.context_finder.utils.intentdetector import detect_intents
from aimodels.context_finder.utils.riskcalculator import calculate_risk

MODEL_NAME = "ThunderCrown/SCAMBERT"

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)


# ============================================================
# LOAD MODEL ONCE
# ============================================================

print("Loading SCAMBERT...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME
)

model.to(device)
model.eval()

print("Device:", device)
print("Labels:", model.config.id2label)
print("Model loaded.\n")


# ============================================================
# SCAM MODEL
# ============================================================

def get_scam_probability(text: str) -> float:
    """
    Returns probability that the text is scam/fraud/phishing.

    Output range:
        0.0 = likely safe
        1.0 = likely scam
    """

    if not text or not text.strip():
        return 0.0

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.inference_mode():
        outputs = model(**inputs)

    probabilities = torch.softmax(
        outputs.logits,
        dim=-1
    )[0]

    # SCAMBERT model card:
    # 0 = Safe
    # 1 = Scam
    scam_probability = probabilities[1].item()

    return scam_probability


def analyze_text(text: str):
    """
    Complete fraud analysis.

    Returns:

    {
        "text": "...",
        "scam_probability": 0.91,
        "intents": {...},
        "risk_score": 0.98,
        "risk_level": "HIGH"
    }
    """

    if not text or not text.strip():
        return {
            "text": text,
            "scam_probability": 0.0,
            "intents": {},
            "risk_score": 0.0,
            "risk_level": "LOW"
        }

    # ML
    scam_probability = get_scam_probability(text)

    # Explicit intents
    intents = detect_intents(text)

    # Combined score
    risk_score = calculate_risk(
        scam_probability,
        intents
    )

    # Risk category
    if risk_score >= 0.80:
        risk_level = "CRITICAL"

    elif risk_score >= 0.60:
        risk_level = "HIGH"

    elif risk_score >= 0.35:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {
        "text": text,
        "scam_probability": scam_probability,
        "intents": intents,
        "risk_score": risk_score,
        "risk_level": risk_level
    }