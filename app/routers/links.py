from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.links import BrokenLink
from app.dependencies import get_current_user
from app.workers.tasks.link_tasks import scan_broken_links_task
from pydantic import BaseModel
from uuid import UUID, uuid4

router = APIRouter()

class LinkScanRequest(BaseModel):
    project_id: str
    domain: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "project_id": "123e4567-e89b-12d3-a456-426614174000",
                "domain": "example.com"
            }
        }

@router.post("/scan",
    summary="Scan for broken links",
    description="Start a background scan to detect broken links on a domain"
)
async def scan_links(
    request: LinkScanRequest,
    background_tasks: BackgroundTasks,
    current_user = Depends(get_current_user)
):
    scan_id = str(uuid4())
    background_tasks.add_task(
        scan_broken_links_task,
        scan_id,
        request.project_id,
        request.domain
    )
    
    return {
        "scan_id": scan_id,
        "status": "queued"
    }

@router.get("/scan/{scan_id}")
async def get_scan_status(scan_id: str):
    return {
        "scan_id": scan_id,
        "status": "completed",
        "progress": 100
    }

@router.get("/{project_id}")
async def get_broken_links(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    broken_links = db.query(BrokenLink).filter(
        BrokenLink.project_id == project_id
    ).all()
    
    return {
        "project_id": str(project_id),
        "broken_links": [
            {
                "source_url": link.source_url,
                "broken_url": link.broken_url,
                "status_code": link.status_code
            }
            for link in broken_links
        ]
    }

@router.get("/{project_id}/export")
async def export_broken_links(
    project_id: UUID,
    current_user = Depends(get_current_user)
):
    return {"message": "Export functionality", "format": "csv"}
