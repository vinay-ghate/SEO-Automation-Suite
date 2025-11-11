from app.workers.celery_app import celery_app
from app.services.competitor_service import CompetitorService
from typing import List

@celery_app.task
def analyze_competitor_task(
    project_id: str,
    competitor_urls: List[str],
    target_url: str
):
    service = CompetitorService()
    
    analysis = service.analyze_competitors(target_url, competitor_urls)
    
    return {
        'project_id': project_id,
        'target_url': target_url,
        'analysis': analysis,
        'status': 'completed'
    }
