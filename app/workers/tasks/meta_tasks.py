from app.workers.celery_app import celery_app
from app.services.meta_generator import MetaGeneratorService
from app.integrations.apify_client import ApifyClient

@celery_app.task
def generate_meta_tags_task(project_id: str, url: str, content: str):
    service = MetaGeneratorService()
    apify_client = ApifyClient()
    
    if url and not content:
        scraped = apify_client.scrape_url(url)
        content = scraped.get('text', '')
    
    result = service.generate_meta_tags(content, url)
    
    return {
        'project_id': project_id,
        'url': url,
        'result': result
    }
