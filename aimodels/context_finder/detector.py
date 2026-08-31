from aimodels.context_finder.utils.audiotranscribe import gettranscribe
from aimodels.context_finder.utils.textcontextdetector import analyze_text


def getcontext_from_audio(audio_path : str):
    """
    Get context from audio file.

    Returns:

    {
        "text": "...",
        "language": "en",
        "duration": 12.34,
        "scam_probability": 0.91,
        "intents": {...},
        "risk_score": 0.98,
        "risk_level": "HIGH"
    }
    """

    # Transcribe audio
    transcription = gettranscribe(audio_path)

    # Analyze text
    analysis = analyze_text(transcription["text"])

    return {
        **transcription,
        **analysis
    }