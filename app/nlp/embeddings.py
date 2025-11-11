from typing import List
import google.generativeai as genai
from app.config import settings

async def generate_embeddings(text: str) -> List[float]:
    try:
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            result = genai.embed_content(
                model="models/embedding-001",
                content=text
            )
            return result['embedding']
    except Exception as e:
        print(f"Embedding error: {e}")
    
    return [0.0] * 768

async def batch_generate_embeddings(texts: List[str]) -> List[List[float]]:
    embeddings = []
    for text in texts:
        embedding = await generate_embeddings(text)
        embeddings.append(embedding)
    return embeddings
