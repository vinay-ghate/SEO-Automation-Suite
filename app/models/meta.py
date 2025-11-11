from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
import uuid
from app.database.base import Base

class MetaTag(Base):
    __tablename__ = "meta_tags"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    url = Column(String)
    input_content = Column(Text)
    variants = Column(JSONB)
    scores = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)
