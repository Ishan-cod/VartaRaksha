from aimodels.recognition_model.utils.generate_embedding import get_embedding
from aimodels.recognition_model.utils.cosine_similiarity import compare_embeddings
from pathlib import Path
import torch

VOICE_DIR = Path(r"aimodels/recognition_model/voices")
THRESHOLD = 0.0
K = 5

def audio_similiarity(audio_path : str):
    embedding = get_embedding(audio_path)

    best_score = -1
    best_match = None

    result = []

    for voice_path in VOICE_DIR.glob("*.pt"):
        compare_embedding = torch.load(voice_path,  map_location="cpu")

        score = compare_embeddings(embedding, compare_embedding)

        if score > THRESHOLD and score > best_score:
            result.append({
                "voice": voice_path.stem,
                "score": score
            })

            best_score = score
            best_match = voice_path.stem

    if best_match is None:
        return {"best_match": "unknown", "best_score": best_score}
    
    result.sort(key=lambda x: x["score"], reverse=True) 

    return {"result": result[:K]}

    

