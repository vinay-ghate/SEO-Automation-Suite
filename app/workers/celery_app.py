from celery import Celery
from app.config import settings

celery_app = Celery(
    'seo_automation',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=[
        'app.workers.tasks.meta_tasks',
        'app.workers.tasks.link_tasks',
        'app.workers.tasks.competitor_tasks',
        'app.workers.tasks.serp_tasks'
    ]
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
