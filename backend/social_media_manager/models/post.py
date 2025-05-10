from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(String, ForeignKey("tenants.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    platform = Column(String)  # twitter, facebook, linkedin, etc.
    scheduled_time = Column(DateTime)
    status = Column(String)  # scheduled, published, failed
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    published_at = Column(DateTime, nullable=True)
    engagements = Column(JSON, nullable=True)  # likes, comments, shares, etc.
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # Relationships
    tenant = relationship("Tenant", back_populates="posts")
    user = relationship("User", back_populates="posts")
    campaign = relationship("Campaign", back_populates="posts")
