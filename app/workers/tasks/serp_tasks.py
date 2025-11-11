from app.workers.celery_app import celery_app
from app.services.serp_service import SerpService
from typing import List

@celery_app.task
def compare_serp_task(
    comparison_id: str,
    project_id: str,
    keywords: List[str],
    location: str
):
    service = SerpService()
    
    results = service.compare_serp(keywords, location)
    
    return {
        'comparison_id': comparison_id,
        'project_id': project_id,
        'results': results,
        'status': 'completed'
    }
