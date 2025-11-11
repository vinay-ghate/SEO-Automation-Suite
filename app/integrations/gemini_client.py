import google.generativeai as genai
from app.config import settings
from typing import List, Dict

class GeminiClient:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def generate_content(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    async def generate_embeddings(self, text: str) -> List[float]:
        return [0.1] * 768
    
    async def analyze_content(self, content: str) -> Dict:
        return {
            'entities': [],
            'keywords': [],
            'sentiment': 'neutral'
        }
