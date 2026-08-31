import os
import torch
from aimodels.recognition_model.utils.generate_embedding import get_embedding

os.makedirs("aimodels/recognition_model/voices", exist_ok=True)

def store_voice(audio_path: str, voice_name: str):
    embedding = get_embedding(audio_path)

    torch.save(
        embedding,
        f"aimodels/recognition_model/voices/{voice_name}_voice.pt"
    )

    print(f"Saved {voice_name}'s voice profile.")
    print("Shape:", embedding.shape)
