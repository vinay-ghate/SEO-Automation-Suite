from typing import List, Dict
from app.integrations.apify_client import ApifyClient
from app.integrations.gemini_client import GeminiClient
from app.nlp.embeddings import generate_embeddings
from app.nlp.similarity import compute_similarity

class CompetitorService:
    def __init__(self):
        self.apify_client = ApifyClient()
        self.gemini_client = GeminiClient()
    
    async def analyze_competitors(
        self,
        target_url: str,
        competitor_urls: List[str]
    ) -> Dict:
        target_content = await self.apify_client.scrape_url(target_url)
        competitor_contents = []
        
        for url in competitor_urls:
            content = await self.apify_client.scrape_url(url)
            competitor_contents.append(content)
        
        target_embedding = await generate_embeddings(target_content['text'])
        competitor_embeddings = [
            await generate_embeddings(c['text'])
            for c in competitor_contents
        ]
        
        similarity_scores = [
            compute_similarity(target_embedding, comp_emb)
            for comp_emb in competitor_embeddings
        ]
        
        avg_similarity = sum(similarity_scores) / len(similarity_scores)
        
        keyword_gap = await self._identify_keyword_gaps(
            target_content,
            competitor_contents
        )
        
        topic_clusters = await self._cluster_topics(competitor_contents)
        
        return {
            'similarity_score': avg_similarity,
            'keyword_gap': keyword_gap,
            'topic_clusters': topic_clusters
        }
    
    async def _identify_keyword_gaps(self, target, competitors) -> List[str]:
        return ['keyword1', 'keyword2', 'keyword3']
    
    async def _cluster_topics(self, contents) -> List[Dict]:
        return [
            {
                'cluster_name': 'Topic 1',
                'topics': ['subtopic1', 'subtopic2']
            }
        ]
