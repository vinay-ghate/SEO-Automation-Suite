from typing import List
import numpy as np

def compute_similarity(embedding1: List[float], embedding2: List[float]) -> float:
    vec1 = np.array(embedding1)
    vec2 = np.array(embedding2)
    
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    similarity = dot_product / (norm1 * norm2)
    return float(similarity)

def compute_batch_similarity(
    target_embedding: List[float],
    embeddings: List[List[float]]
) -> List[float]:
    similarities = []
    for embedding in embeddings:
        sim = compute_similarity(target_embedding, embedding)
        similarities.append(sim)
    return similarities
