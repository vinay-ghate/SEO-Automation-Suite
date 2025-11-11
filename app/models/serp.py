from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from app.database.base import Base

class SerpHistory(Base):
    __tablename__ = "serp_history"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    keyword = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    rank = Column(Integer)
    detected_at = Column(DateTime, default=datetime.utcnow)
