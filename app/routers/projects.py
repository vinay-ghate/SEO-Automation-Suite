from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.project import Project
from app.models.user import User
from app.dependencies import get_current_user
from pydantic import BaseModel
from typing import List
from uuid import UUID

router = APIRouter()

class ProjectCreate(BaseModel):
    name: str
    domain: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "My Website SEO",
                "domain": "example.com"
            }
        }

class ProjectResponse(BaseModel):
    project_id: str
    name: str
    domain: str
    created_at: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "project_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "My Website SEO",
                "domain": "example.com",
                "created_at": "2024-01-15T10:30:00"
            }
        }

@router.post("", 
    response_model=ProjectResponse,
    summary="Create a new project",
    description="Create a new SEO project for tracking and analysis"
)
async def create_project(
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = Project(
        name=request.name,
        domain=request.domain,
        owner_id=current_user.id
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    
    return {
        "project_id": str(project.id),
        "name": project.name,
        "domain": project.domain,
        "created_at": project.created_at.isoformat()
    }

@router.get("", 
    response_model=List[ProjectResponse],
    summary="List all projects",
    description="Get all projects owned by the authenticated user"
)
async def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    projects = db.query(Project).filter(Project.owner_id == current_user.id).all()
    return [
        {
            "project_id": str(p.id),
            "name": p.name,
            "domain": p.domain,
            "created_at": p.created_at.isoformat()
        }
        for p in projects
    ]

@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return {
        "project_id": str(project.id),
        "name": project.name,
        "domain": project.domain,
        "created_at": project.created_at.isoformat()
    }

@router.put("/{project_id}")
async def update_project(
    project_id: UUID,
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project.name = request.name
    project.domain = request.domain
    db.commit()
    
    return {"message": "Project updated successfully"}

@router.delete("/{project_id}")
async def delete_project(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db.delete(project)
    db.commit()
    
    return {"message": "Project deleted successfully"}

@router.post("/{project_id}/invite")
async def invite_to_project(project_id: UUID):
    return {"message": "Invitation sent"}
