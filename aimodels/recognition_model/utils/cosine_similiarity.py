import torch
import torch.nn.functional as F

def compare_embeddings(
    embedding1: torch.Tensor,
    embedding2: torch.Tensor
) -> float:

    embedding1 = embedding1.unsqueeze(0)
    embedding2 = embedding2.unsqueeze(0)

    return F.cosine_similarity(
        embedding1,
        embedding2
    ).item()