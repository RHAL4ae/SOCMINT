from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    tenant_id = Column(String, ForeignKey("tenants.id"))

    # Relationships
    tenant = relationship("Tenant", back_populates="users")
    posts = relationship("Post", back_populates="user")
