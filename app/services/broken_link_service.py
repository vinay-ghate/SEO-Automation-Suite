from typing import List, Dict
from app.integrations.apify_client import ApifyClient

class BrokenLinkService:
    def __init__(self):
        self.apify_client = ApifyClient()
    
    async def scan_domain(self, domain: str) -> List[Dict]:
        crawl_results = await self.apify_client.crawl_website(domain)
        
        broken_links = []
        for page in crawl_results:
            for link in page.get('links', []):
                if link.get('status_code', 200) >= 400:
                    broken_links.append({
                        'source_url': page['url'],
                        'broken_url': link['url'],
                        'status_code': link['status_code']
                    })
        
        return broken_links
    
    async def check_redirect_chains(self, url: str) -> Dict:
        return {
            'url': url,
            'redirect_chain': [],
            'final_status': 200
        }
