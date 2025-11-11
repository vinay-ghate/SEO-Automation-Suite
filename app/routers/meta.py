from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.meta import MetaTag
from app.dependencies import get_current_user
from app.workers.tasks.meta_tasks import generate_meta_tags_task
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID

router = APIRouter()

class MetaGenerateRequest(BaseModel):
    project_id: str
    url: Optional[str] = None
    content: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "project_id": "123e4567-e89b-12d3-a456-426614174000",
                "url": "https://example.com/page",
                "content": "Optional page content for analysis"
            }
        }

@router.post("/generate",
    summary="Generate meta tags",
    description="Generate AI-powered meta tags for a URL or content using Gemini"
)
async def generate_meta(
    request: MetaGenerateRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    background_tasks.add_task(
        generate_meta_tags_task,
        request.project_id,
        request.url,
        request.content
    )
    
    return {
        "message": "Meta tag generation started",
        "status": "processing"
    }

@router.get("/{project_id}")
async def get_meta_tags(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    meta_tags = db.query(MetaTag).filter(MetaTag.project_id == project_id).all()
    return {"meta_tags": meta_tags}

@router.get("/{project_id}/{meta_id}")
async def get_meta_tag(
    project_id: UUID,
    meta_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    meta_tag = db.query(MetaTag).filter(
        MetaTag.id == meta_id,
        MetaTag.project_id == project_id
    ).first()
    
    if not meta_tag:
        raise HTTPException(status_code=404, detail="Meta tag not found")
    
    return meta_tag

@router.delete("/{project_id}/{meta_id}")
async def delete_meta_tag(
    project_id: UUID,
    meta_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    meta_tag = db.query(MetaTag).filter(
        MetaTag.id == meta_id,
        MetaTag.project_id == project_id
    ).first()
    
    if not meta_tag:
        raise HTTPException(status_code=404, detail="Meta tag not found")
    
    db.delete(meta_tag)
    db.commit()
    
    return {"message": "Meta tag deleted successfully"}
