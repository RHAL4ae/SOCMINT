from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from database import Base

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(String, ForeignKey("tenants.id"))
    name = Column(String)
    description = Column(String, nullable=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    metrics = Column(JSON)  # campaign-level metrics
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # Relationships
    tenant = relationship("Tenant", back_populates="campaigns")
    posts = relationship("Post", back_populates="campaign")
