from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.competitor import CompetitorAnalysis
from app.dependencies import get_current_user
from app.workers.tasks.competitor_tasks import analyze_competitor_task
from pydantic import BaseModel
from typing import List
from uuid import UUID

router = APIRouter()

class CompetitorAnalyzeRequest(BaseModel):
    project_id: str
    competitor_urls: List[str]
    target_url: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "project_id": "123e4567-e89b-12d3-a456-426614174000",
                "competitor_urls": [
                    "https://competitor1.com",
                    "https://competitor2.com"
                ],
                "target_url": "https://mysite.com"
            }
        }

@router.post("/analyze",
    summary="Analyze competitors",
    description="Perform AI-powered competitor content analysis and identify keyword gaps"
)
async def analyze_competitor(
    request: CompetitorAnalyzeRequest,
    background_tasks: BackgroundTasks,
    current_user = Depends(get_current_user)
):
    background_tasks.add_task(
        analyze_competitor_task,
        request.project_id,
        request.competitor_urls,
        request.target_url
    )
    
    return {
        "message": "Competitor analysis started",
        "status": "processing"
    }

@router.get("/{project_id}")
async def get_competitor_analyses(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    analyses = db.query(CompetitorAnalysis).filter(
        CompetitorAnalysis.project_id == project_id
    ).all()
    
    return {"analyses": analyses}

@router.get("/report/{analysis_id}")
async def get_analysis_report(
    analysis_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    analysis = db.query(CompetitorAnalysis).filter(
        CompetitorAnalysis.id == analysis_id
    ).first()
    
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    return {
        "analysis_id": str(analysis.id),
        "similarity_score": analysis.similarity_score,
        "keyword_gap": analysis.keyword_gap,
        "topic_clusters": analysis.topic_clusters
    }

@router.delete("/report/{analysis_id}")
async def delete_analysis(
    analysis_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    analysis = db.query(CompetitorAnalysis).filter(
        CompetitorAnalysis.id == analysis_id
    ).first()
    
    if not analysis:
        raise HTTPException(status_code=404, detail="Analysis not found")
    
    db.delete(analysis)
    db.commit()
    
    return {"message": "Analysis deleted successfully"}
