# SOCMINT UAE PASS Authentication Service (FastAPI)
# This module implements OAuth2 Authorization Code Flow with PKCE for UAE PASS integration.
# Endpoints: /auth/uaepass/login, /auth/uaepass/callback, /auth/profile, /auth/logout

from fastapi import FastAPI, APIRouter, Request, Response, HTTPException, status, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import jwt, JWTError
import httpx
import os
import secrets
import base64
import hashlib
from typing import Optional

router = APIRouter()

UAE_PASS_CLIENT_ID = os.getenv("UAE_PASS_CLIENT_ID")
UAE_PASS_CLIENT_SECRET = os.getenv("UAE_PASS_CLIENT_SECRET")
UAE_PASS_AUTH_URL = os.getenv("UAE_PASS_AUTH_URL", "https://stg-id.uaepass.ae/idshub/authorize")
UAE_PASS_TOKEN_URL = os.getenv("UAE_PASS_TOKEN_URL", "https://stg-id.uaepass.ae/idshub/token")
UAE_PASS_USERINFO_URL = os.getenv("UAE_PASS_USERINFO_URL", "https://stg-id.uaepass.ae/idshub/userinfo")
REDIRECT_URI = os.getenv("REDIRECT_URI", "https://socmint.ae/auth/uaepass/callback")
SOCMINT_JWT_SECRET = os.getenv("SOCMINT_JWT_SECRET", "change_this_secret")
SOCMINT_JWT_ALGORITHM = "HS256"

# In-memory store for PKCE and nonce (for demo; use persistent store in production)
session_store = {}

def generate_pkce_pair():
    code_verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b'=').decode('utf-8')
    code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode()).digest()).rstrip(b'=').decode('utf-8')
    return code_verifier, code_challenge

def generate_nonce():
    return secrets.token_urlsafe(16)

@router.get("/auth/uaepass/login")
def uaepass_login(request: Request):
    code_verifier, code_challenge = generate_pkce_pair()
    nonce = generate_nonce()
    state = secrets.token_urlsafe(16)
    # Store PKCE and nonce for this state
    session_store[state] = {"code_verifier": code_verifier, "nonce": nonce}
    params = {
        "client_id": UAE_PASS_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "openid profile email phone",
        "state": state,
        "nonce": nonce,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256"
    }
    url = httpx.URL(UAE_PASS_AUTH_URL).copy_add_params(params)
    return RedirectResponse(str(url))

@router.get("/auth/uaepass/callback")
def uaepass_callback(request: Request, code: str = None, state: str = None):
    if not code or not state or state not in session_store:
        raise HTTPException(status_code=400, detail="Invalid callback parameters.")
    code_verifier = session_store[state]["code_verifier"]
    nonce = session_store[state]["nonce"]
    # Exchange code for tokens
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": UAE_PASS_CLIENT_ID,
        "code_verifier": code_verifier
    }
    auth = (UAE_PASS_CLIENT_ID, UAE_PASS_CLIENT_SECRET)
    with httpx.Client() as client:
        token_resp = client.post(UAE_PASS_TOKEN_URL, data=data, auth=auth)
        if token_resp.status_code != 200:
            raise HTTPException(status_code=401, detail="Token exchange failed.")
        tokens = token_resp.json()
        id_token = tokens.get("id_token")
        access_token = tokens.get("access_token")
        # Validate ID token (nonce, audience, expiration)
        try:
            payload = jwt.decode(id_token, key=None, options={"verify_signature": False})
            if payload.get("nonce") != nonce:
                raise HTTPException(status_code=401, detail="Invalid nonce.")
            if payload.get("aud") != UAE_PASS_CLIENT_ID:
                raise HTTPException(status_code=401, detail="Invalid audience.")
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid ID token.")
        # Retrieve user info
        headers = {"Authorization": f"Bearer {access_token}"}
        userinfo_resp = client.get(UAE_PASS_USERINFO_URL, headers=headers)
        if userinfo_resp.status_code != 200:
            raise HTTPException(status_code=401, detail="Failed to fetch user info.")
        userinfo = userinfo_resp.json()
        # Extract user data
        emirates_id = userinfo.get("national_id")
        full_name = userinfo.get("name")
        mobile = userinfo.get("phone")
        email = userinfo.get("email")
        # Map to SOCMINT user (stub: replace with real lookup/creation)
        tenant_id = "demo_tenant"
        user_id = emirates_id or "demo_user"
        role = "user"
        # Issue SOCMINT JWT
        socmint_payload = {
            "tenant_id": tenant_id,
            "user_id": user_id,
            "role": role,
            "name": full_name,
            "national_id": emirates_id,
            "email": email,
            "phone": mobile
        }
        socmint_jwt = jwt.encode(socmint_payload, SOCMINT_JWT_SECRET, algorithm=SOCMINT_JWT_ALGORITHM)
        # Log login attempt (stub)
        print(f"Login: {user_id} ({full_name})")
        # Return JWT to frontend (could be via redirect with token or set-cookie)
        return JSONResponse({"jwt": socmint_jwt, "user": socmint_payload})

@router.get("/auth/profile")
def get_profile(token: str = Depends(OAuth2AuthorizationCodeBearer(authorizationUrl="/auth/uaepass/login", tokenUrl="/auth/uaepass/callback"))):
    try:
        payload = jwt.decode(token, SOCMINT_JWT_SECRET, algorithms=[SOCMINT_JWT_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token.")

@router.post("/auth/logout")
def logout():
    # Invalidate session (stateless JWT, so just inform frontend to delete token)
    return {"message": "Logged out."}

# FastAPI app registration
app = FastAPI()
app.include_router(router)