from typing import List, Dict
from app.integrations.apify_client import ApifyClient

class SerpService:
    def __init__(self):
        self.apify_client = ApifyClient()
    
    async def compare_serp(
        self,
        keywords: List[str],
        location: str
    ) -> Dict:
        results = []
        
        for keyword in keywords:
            serp_data = await self.apify_client.fetch_serp(keyword, location)
            
            rankings = []
            for idx, result in enumerate(serp_data.get('organic_results', []), 1):
                rankings.append({
                    'domain': result.get('domain'),
                    'position': idx,
                    'url': result.get('url'),
                    'title': result.get('title')
                })
            
            results.append({
                'keyword': keyword,
                'rankings': rankings
            })
        
        return {'results': results}
    
    async def get_rank_history(self, keyword: str, domain: str) -> List[Dict]:
        return [
            {'date': '2024-01-01', 'rank': 5},
            {'date': '2024-01-15', 'rank': 3}
        ]
