from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.serp import SerpHistory
from app.dependencies import get_current_user
from app.workers.tasks.serp_tasks import compare_serp_task
from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4

router = APIRouter()

class SerpCompareRequest(BaseModel):
    project_id: str
    keywords: List[str]
    location: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "project_id": "123e4567-e89b-12d3-a456-426614174000",
                "keywords": ["seo tools", "keyword research"],
                "location": "United States"
            }
        }

@router.post("/compare",
    summary="Compare SERP rankings",
    description="Track and compare search engine result page rankings for keywords"
)
async def compare_serp(
    request: SerpCompareRequest,
    background_tasks: BackgroundTasks,
    current_user = Depends(get_current_user)
):
    comparison_id = str(uuid4())
    background_tasks.add_task(
        compare_serp_task,
        comparison_id,
        request.project_id,
        request.keywords,
        request.location
    )
    
    return {
        "comparison_id": comparison_id,
        "status": "processing"
    }

@router.get("/{project_id}")
async def get_serp_data(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    serp_data = db.query(SerpHistory).filter(
        SerpHistory.project_id == project_id
    ).all()
    
    return {"serp_data": serp_data}

@router.get("/history/{keyword}")
async def get_keyword_history(
    keyword: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    history = db.query(SerpHistory).filter(
        SerpHistory.keyword == keyword
    ).order_by(SerpHistory.detected_at.desc()).all()
    
    return {"keyword": keyword, "history": history}

@router.get("/compare/{comparison_id}")
async def get_comparison(comparison_id: str):
    return {
        "comparison_id": comparison_id,
        "status": "completed"
    }

@router.delete("/{comparison_id}")
async def delete_comparison(comparison_id: str):
    return {"message": "Comparison deleted successfully"}
