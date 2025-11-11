from app.workers.celery_app import celery_app
from app.services.broken_link_service import BrokenLinkService

@celery_app.task
def scan_broken_links_task(scan_id: str, project_id: str, domain: str):
    service = BrokenLinkService()
    
    broken_links = service.scan_domain(domain)
    
    return {
        'scan_id': scan_id,
        'project_id': project_id,
        'broken_links': broken_links,
        'status': 'completed'
    }
