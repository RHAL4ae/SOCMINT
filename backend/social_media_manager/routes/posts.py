from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from models.database import get_db
from models.post import Post
from models.campaign import Campaign

router = APIRouter()

@router.post("/schedule")
async def schedule_post(
    content: str,
    platform: str,
    scheduled_time: datetime,
    campaign_id: Optional[int] = None,
    tenant_id: str = Depends(verify_jwt),
    db: Session = Depends(get_db)
):
    """
    Schedule a new post
    """
    post = Post(
        tenant_id=tenant_id,
        content=content,
        platform=platform,
        scheduled_time=scheduled_time,
        status="scheduled",
        campaign_id=campaign_id
    )
    
    db.add(post)
    db.commit()
    db.refresh(post)
    
    # TODO: Add to scheduler
    return {"message": "Post scheduled successfully", "post_id": post.id}

@router.get("/posts")
async def get_posts(
    tenant_id: str = Depends(verify_jwt),
    db: Session = Depends(get_db),
    status: Optional[str] = None,
    platform: Optional[str] = None,
    campaign_id: Optional[int] = None
):
    """
    Get all posts for a tenant
    """
    query = db.query(Post).filter(Post.tenant_id == tenant_id)
    
    if status:
        query = query.filter(Post.status == status)
    if platform:
        query = query.filter(Post.platform == platform)
    if campaign_id:
        query = query.filter(Post.campaign_id == campaign_id)
    
    posts = query.all()
    return posts

@router.get("/posts/{post_id}")
async def get_post(
    post_id: int,
    tenant_id: str = Depends(verify_jwt),
    db: Session = Depends(get_db)
):
    """
    Get a specific post
    """
    post = db.query(Post).filter(
        Post.id == post_id,
        Post.tenant_id == tenant_id
    ).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return post
