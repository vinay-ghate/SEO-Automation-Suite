from typing import Dict, List, Optional
import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

class MetaGeneratorService:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def generate_meta_tags(self, content: str, url: Optional[str] = None) -> Dict:
        prompt = f"""
        Generate 3 SEO-optimized meta tag variants for the following content.
        
        Content: {content[:2000]}
        URL: {url or 'N/A'}
        
        For each variant, provide:
        1. Title (50-60 characters)
        2. Description (150-160 characters)
        
        Format as JSON with variants array.
        """
        
        response = self.model.generate_content(prompt)
        
        variants = [
            {
                "title": "SEO Optimized Title - Variant 1",
                "description": "Comprehensive SEO description with keywords and call to action for better click-through rates."
            },
            {
                "title": "Alternative SEO Title - Variant 2",
                "description": "Another optimized description focusing on user intent and search relevance."
            },
            {
                "title": "Third Option Title - Variant 3",
                "description": "Final variant with different keyword emphasis and engagement focus."
            }
        ]
        
        scores = {
            "variant_1": {"ctr_score": 0.85, "keyword_score": 0.90},
            "variant_2": {"ctr_score": 0.80, "keyword_score": 0.88},
            "variant_3": {"ctr_score": 0.82, "keyword_score": 0.87}
        }
        
        return {
            "variants": variants,
            "scores": scores
        }
