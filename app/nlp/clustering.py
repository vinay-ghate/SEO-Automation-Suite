from typing import List, Dict
from sklearn.cluster import KMeans
import numpy as np

def cluster_topics(embeddings: List[List[float]], n_clusters: int = 5) -> List[Dict]:
    if len(embeddings) < n_clusters:
        n_clusters = len(embeddings)
    
    X = np.array(embeddings)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X)
    
    clusters = []
    for i in range(n_clusters):
        cluster_indices = np.where(labels == i)[0]
        clusters.append({
            'cluster_id': i,
            'size': len(cluster_indices),
            'indices': cluster_indices.tolist()
        })
    
    return clusters

def identify_topic_keywords(cluster_texts: List[str]) -> List[str]:
    return ['keyword1', 'keyword2', 'keyword3']
