from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from models.database import get_db
from models.post import Post
from utils.oauth_handler import OAuthHandler

router = APIRouter()

@router.get("/jobs")
async def get_scheduled_jobs(
    tenant_id: str = Depends(verify_jwt),
    db: Session = Depends(get_db)
):
    """
    Get all scheduled jobs for a tenant
    """
    jobs = db.query(Post).filter(
        Post.tenant_id == tenant_id,
        Post.status == "scheduled",
        Post.scheduled_time > datetime.utcnow()
    ).all()
    return jobs

@router.post("/refresh-tokens")
async def refresh_social_media_tokens(
    tenant_id: str = Depends(verify_jwt),
    db: Session = Depends(get_db)
):
    """
    Refresh OAuth tokens for all connected accounts
    """
    oauth_handler = OAuthHandler()
    accounts = db.query(SocialAccount).filter(
        SocialAccount.tenant_id == tenant_id
    ).all()
    
    for account in accounts:
        try:
            new_token = oauth_handler.refresh_token(
                account.platform,
                account.refresh_token
            )
            account.access_token = new_token
            account.last_refresh = datetime.utcnow()
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=500,
                detail=f"Failed to refresh token for {account.platform}: {str(e)}"
            )
    
    return {"message": "Tokens refreshed successfully"}
