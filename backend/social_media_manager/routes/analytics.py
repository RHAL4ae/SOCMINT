from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from models.database import get_db
from models.campaign import Campaign
from models.post import Post

router = APIRouter()

@router.get("/analytics/campaign/{campaign_id}")
async def get_campaign_analytics(
    campaign_id: int,
    tenant_id: str = Depends(verify_jwt),
    db: Session = Depends(get_db),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    """
    Get analytics for a specific campaign
    """
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id,
        Campaign.tenant_id == tenant_id
    ).first()
    
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    # Query posts for this campaign
    query = db.query(Post).filter(
        Post.campaign_id == campaign_id,
        Post.tenant_id == tenant_id
    )
    
    if start_date:
        query = query.filter(Post.scheduled_time >= start_date)
    if end_date:
        query = query.filter(Post.scheduled_time <= end_date)
    
    posts = query.all()
    
    # Calculate metrics
    total_posts = len(posts)
    total_engagements = sum(p.engagements for p in posts if p.engagements)
    average_engagement = total_engagements / total_posts if total_posts else 0
    
    return {
        "campaign_id": campaign_id,
        "total_posts": total_posts,
        "total_engagements": total_engagements,
        "average_engagement": average_engagement,
        "metrics_by_platform": campaign.metrics
    }

@router.get("/analytics/overview")
async def get_tenant_analytics(
    tenant_id: str = Depends(verify_jwt),
    db: Session = Depends(get_db),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
):
    """
    Get overview analytics for a tenant
    """
    # Query all campaigns for this tenant
    query = db.query(Campaign).filter(Campaign.tenant_id == tenant_id)
    
    if start_date:
        query = query.filter(Campaign.start_date >= start_date)
    if end_date:
        query = query.filter(Campaign.end_date <= end_date)
    
    campaigns = query.all()
    
    # Calculate overall metrics
    total_campaigns = len(campaigns)
    total_engagements = sum(
        sum(p.engagements for p in c.posts if p.engagements)
        for c in campaigns
    )
    
    return {
        "total_campaigns": total_campaigns,
        "total_engagements": total_engagements,
        "campaigns": [
            {
                "id": c.id,
                "name": c.name,
                "total_engagements": sum(
                    p.engagements for p in c.posts if p.engagements
                )
            }
            for c in campaigns
        ]
    }
