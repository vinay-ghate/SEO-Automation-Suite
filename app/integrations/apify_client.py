import httpx
from typing import Dict, List
from app.config import settings

class ApifyClient:
    def __init__(self):
        self.api_token = settings.APIFY_API_TOKEN
        self.api_url = settings.APIFY_API_URL
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
    
    async def crawl_website(self, domain: str) -> List[Dict]:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/acts/apify~website-content-crawler/runs",
                headers=self.headers,
                json={"startUrls": [{"url": f"https://{domain}"}]}
            )
            return []
    
    async def scrape_url(self, url: str) -> Dict:
        return {
            'url': url,
            'text': 'Scraped content',
            'headings': [],
            'metadata': {}
        }
    
    async def fetch_serp(self, keyword: str, location: str) -> Dict:
        return {
            'keyword': keyword,
            'location': location,
            'organic_results': []
        }
