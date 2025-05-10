from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from requests_oauthlib import OAuth2Session
from pydantic import BaseModel
from typing import Optional
import os
from datetime import datetime, timedelta
from jose import jwt
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# OAuth2 Configuration
UAEPASS_CLIENT_ID = os.getenv("UAE_PASS_CLIENT_ID")
UAEPASS_CLIENT_SECRET = os.getenv("UAE_PASS_CLIENT_SECRET")
UAEPASS_AUTH_URL = os.getenv("UAE_PASS_AUTH_URL")
UAEPASS_TOKEN_URL = os.getenv("UAE_PASS_TOKEN_URL")
UAEPASS_USERINFO_URL = os.getenv("UAE_PASS_USERINFO_URL")
REDIRECT_URI = os.getenv("REDIRECT_URI")

oauth = OAuth2Session(UAEPASS_CLIENT_ID, redirect_uri=REDIRECT_URI)

# JWT Configuration
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_MINUTES = 60

class UserProfile(BaseModel):
    emirates_id: str
    full_name: str
    mobile_number: str
    email: str
    tenant_id: str
    user_id: str
    role: str

@router.get("/auth/uaepass/login")
async def uaepass_login():
    authorization_url, state = oauth.authorization_url(
        UAEPASS_AUTH_URL,
        scope="openid profile email phone address",
        state=os.urandom(16).hex()
    )
    return {"authorization_url": authorization_url}

@router.get("/auth/uaepass/callback")
async def uaepass_callback(code: str, state: str):
    try:
        token = oauth.fetch_token(
            UAEPASS_TOKEN_URL,
            client_secret=UAEPASS_CLIENT_SECRET,
            code=code
        )
        
        # Get user info
        userinfo = oauth.get(UAEPASS_USERINFO_URL).json()
        
        # Map UAE PASS user to internal user
        user_profile = await map_user_to_internal(userinfo)
        
        # Create JWT token
        access_token = create_jwt_token(user_profile)
        
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )

async def map_user_to_internal(userinfo: dict) -> UserProfile:
    # This is a placeholder - implement your actual mapping logic here
    return UserProfile(
        emirates_id=userinfo.get("sub"),
        full_name=f"{userinfo.get('given_name')} {userinfo.get('family_name')}",
        mobile_number=userinfo.get("phone_number"),
        email=userinfo.get("email"),
        tenant_id="default",  # Replace with actual tenant mapping
        user_id=userinfo.get("sub"),  # Using sub as user_id
        role="user"  # Replace with actual role mapping
    )

def create_jwt_token(user_profile: UserProfile) -> str:
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    to_encode = {
        "sub": user_profile.user_id,
        "tenant_id": user_profile.tenant_id,
        "role": user_profile.role,
        "exp": expire,
        "iat": datetime.utcnow()
    }
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

@router.get("/auth/profile")
async def get_profile():
    # TODO: Implement profile retrieval
    pass

@router.post("/auth/logout")
async def logout():
    # TODO: Implement logout
    pass
