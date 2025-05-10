from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    domain = Column(String, unique=True)
    created_at = Column(Integer)  # Unix timestamp

    # Relationships
    users = relationship("User", back_populates="tenant")
    social_accounts = relationship("SocialAccount", back_populates="tenant")
    posts = relationship("Post", back_populates="tenant")
    campaigns = relationship("Campaign", back_populates="tenant")
