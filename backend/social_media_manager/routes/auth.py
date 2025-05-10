from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from jose import jwt
from datetime import datetime, timedelta

from models.database import get_db
from models.user import User
from models.tenant import Tenant
from utils.token_verification import verify_jwt

router = APIRouter()

@router.post("/connect/account/{platform}")
async def connect_social_account(platform: str, token: str, tenant_id: str, db: Session = Depends(get_db)):
    """
    Connect a social media account for a tenant
    """
    # Verify tenant exists
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    # TODO: Implement platform-specific OAuth verification
    # For now, we'll assume token is valid
    
    # Store the token in the database
    social_account = SocialAccount(
        tenant_id=tenant_id,
        platform=platform,
        access_token=token,
        last_refresh=datetime.utcnow()
    )
    db.add(social_account)
    db.commit()
    db.refresh(social_account)

    return {"message": "Account connected successfully", "account_id": social_account.id}

@router.get("/accounts")
async def get_social_accounts(tenant_id: str, db: Session = Depends(get_db)):
    """
    Get all connected social media accounts for a tenant
    """
    accounts = db.query(SocialAccount).filter(SocialAccount.tenant_id == tenant_id).all()
    return accounts

@router.delete("/accounts/{account_id}")
async def disconnect_social_account(account_id: int, tenant_id: str, db: Session = Depends(get_db)):
    """
    Disconnect a social media account
    """
    account = db.query(SocialAccount).filter(
        SocialAccount.id == account_id,
        SocialAccount.tenant_id == tenant_id
    ).first()
    
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    
    db.delete(account)
    db.commit()
    return {"message": "Account disconnected successfully"}
