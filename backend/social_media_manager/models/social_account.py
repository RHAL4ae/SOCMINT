from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class SocialAccount(Base):
    __tablename__ = "social_accounts"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(String, ForeignKey("tenants.id"))
    platform = Column(String)  # twitter, facebook, linkedin, etc.
    access_token = Column(String)
    refresh_token = Column(String)
    last_refresh = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # Relationships
    tenant = relationship("Tenant", back_populates="social_accounts")
