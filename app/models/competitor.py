from sqlalchemy import Column, String, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
import uuid
from app.database.base import Base

class CompetitorAnalysis(Base):
    __tablename__ = "competitor_analysis"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    target_url = Column(String, nullable=False)
    competitor_urls = Column(JSONB)
    similarity_score = Column(Float)
    keyword_gap = Column(JSONB)
    topic_clusters = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)
