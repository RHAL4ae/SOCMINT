from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

# Import routes
from routes.auth import router as auth_router
from routes.posts import router as posts_router
from routes.scheduler import router as scheduler_router
from routes.analytics import router as analytics_router

# Import database
from models.database import engine, Base, get_db

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="SOCMINT Social Media Manager",
    description="Multi-tenant social media management microservice for SOCMINT platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "*")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api/v1", tags=["Authentication"])
app.include_router(posts_router, prefix="/api/v1", tags=["Posts"])
app.include_router(scheduler_router, prefix="/api/v1", tags=["Scheduler"])
app.include_router(analytics_router, prefix="/api/v1", tags=["Analytics"])

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to SOCMINT Social Media Manager API",
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)