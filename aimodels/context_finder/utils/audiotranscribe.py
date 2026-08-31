from faster_whisper import WhisperModel

model = WhisperModel(
    "Systran/faster-distil-whisper-small.en",
    device="cpu",
    compute_type="int8"
)

def gettranscribe(audio_path : str) : 
    segments, info = model.transcribe(
        audio_path,
        language="en",
        beam_size=1,
        vad_filter=True
    )

    text = " ".join(
        segment.text.strip()
        for segment in segments
    )

    return {
        "text": text,
        "language": info.language,
        "duration": info.duration,
    }
