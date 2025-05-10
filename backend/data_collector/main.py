import os
import asyncio
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Depends, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Import collectors
from collectors.facebook_collector import FacebookCollector
from collectors.twitter_collector import TwitterCollector
from collectors.reddit_collector import RedditCollector
from collectors.instagram_collector import InstagramCollector

# Import scrapers
from scraper.regular_scraper import RegularScraper
from scraper.darkweb_scraper import DarkWebScraper

# Import utility functions
from utils.helpers import check_kafka_connection

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="OSINT Data Collector",
    description="A microservice for collecting data from various OSINT sources",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize collectors
facebook_collector = FacebookCollector()
twitter_collector = TwitterCollector()
reddit_collector = RedditCollector()
instagram_collector = InstagramCollector()

# Initialize scrapers
regular_scraper = RegularScraper()
darkweb_scraper = DarkWebScraper()

# Define request models
class SocialMediaRequest(BaseModel):
    """Base model for social media collection requests"""
    limit: Optional[int] = 25

class FacebookRequest(SocialMediaRequest):
    """Facebook collection request model"""
    page_id: Optional[str] = None
    post_id: Optional[str] = None

class TwitterRequest(SocialMediaRequest):
    """Twitter collection request model"""
    query: Optional[str] = None
    username: Optional[str] = None
    tweet_id: Optional[str] = None
    max_results: Optional[int] = 25

class RedditRequest(SocialMediaRequest):
    """Reddit collection request model"""
    subreddit: Optional[str] = None
    post_id: Optional[str] = None
    search_query: Optional[str] = None
    sort: Optional[str] = "new"

class InstagramRequest(SocialMediaRequest):
    """Instagram collection request model"""
    user_id: Optional[str] = None
    media_id: Optional[str] = None
    hashtag: Optional[str] = None

class ScrapeRequest(BaseModel):
    """Web scraping request model"""
    url: str
    method: Optional[str] = "selenium"  # selenium, scrapy, requests
    selectors: Optional[Dict[str, str]] = None
    wait_for: Optional[str] = None  # CSS selector to wait for
    timeout: Optional[int] = 30  # seconds

class DarkWebScrapeRequest(BaseModel):
    """Dark web scraping request model"""
    url: str
    method: Optional[str] = "requests"  # selenium, requests
    selectors: Optional[Dict[str, str]] = None
    timeout: Optional[int] = 60  # seconds

class StatusResponse(BaseModel):
    """Status response model"""
    status: str
    kafka_connection: bool
    collectors: Dict[str, bool]
    scrapers: Dict[str, bool]

# Define API endpoints
@app.get("/")
async def root():
    """Root endpoint to check if the API is running"""
    return {"status": "OSINT Data Collector API is running"}

@app.get("/status", response_model=StatusResponse)
async def get_status():
    """Get the status of all collectors and scrapers"""
    # Check Kafka connection
    kafka_status = check_kafka_connection()
    
    # Check collectors
    collectors_status = {
        "facebook": facebook_collector.check_connection(),
        "twitter": twitter_collector.check_connection(),
        "reddit": reddit_collector.check_connection(),
        "instagram": instagram_collector.check_connection()
    }
    
    # Check scrapers
    scrapers_status = {
        "regular": all(regular_scraper.check_status().values()),
        "darkweb": darkweb_scraper.check_status()
    }
    
    # Determine overall status
    if kafka_status and any(collectors_status.values()) and any(scrapers_status.values()):
        status = "healthy"
    elif kafka_status and (any(collectors_status.values()) or any(scrapers_status.values())):
        status = "degraded"
    else:
        status = "unhealthy"
    
    return StatusResponse(
        status=status,
        kafka_connection=kafka_status,
        collectors=collectors_status,
        scrapers=scrapers_status
    )

@app.post("/collect/facebook")
async def collect_facebook(request: FacebookRequest):
    """Collect data from Facebook"""
    result = await facebook_collector.collect(request.dict())
    if result:
        return {"status": "success", "message": "Facebook data collection completed"}
    raise HTTPException(status_code=500, detail="Facebook data collection failed")

@app.post("/collect/twitter")
async def collect_twitter(request: TwitterRequest):
    """Collect data from Twitter"""
    result = await twitter_collector.collect(request.dict())
    if result:
        return {"status": "success", "message": "Twitter data collection completed"}
    raise HTTPException(status_code=500, detail="Twitter data collection failed")

@app.post("/collect/reddit")
async def collect_reddit(request: RedditRequest):
    """Collect data from Reddit"""
    result = await reddit_collector.collect(request.dict())
    if result:
        return {"status": "success", "message": "Reddit data collection completed"}
    raise HTTPException(status_code=500, detail="Reddit data collection failed")

@app.post("/collect/instagram")
async def collect_instagram(request: InstagramRequest):
    """Collect data from Instagram"""
    result = await instagram_collector.collect(request.dict())
    if result:
        return {"status": "success", "message": "Instagram data collection completed"}
    raise HTTPException(status_code=500, detail="Instagram data collection failed")

@app.post("/collect/{platform}")
async def collect_generic(platform: str, request: dict):
    """Generic collection endpoint for any platform"""
    if platform == "facebook":
        result = await facebook_collector.collect(request)
    elif platform == "twitter":
        result = await twitter_collector.collect(request)
    elif platform == "reddit":
        result = await reddit_collector.collect(request)
    elif platform == "instagram":
        result = await instagram_collector.collect(request)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported platform: {platform}")
    
    if result:
        return {"status": "success", "message": f"{platform.capitalize()} data collection completed"}
    raise HTTPException(status_code=500, detail=f"{platform.capitalize()} data collection failed")

@app.post("/scrape")
async def scrape_website(request: ScrapeRequest):
    """Scrape a website"""
    result = await regular_scraper.scrape(request.dict())
    if result:
        return {"status": "success", "message": "Web scraping completed"}
    raise HTTPException(status_code=500, detail="Web scraping failed")

@app.post("/scrape/darkweb")
async def scrape_darkweb(request: DarkWebScrapeRequest):
    """Scrape a dark web site"""
    # Check TOR connection first
    if not darkweb_scraper.check_status():
        raise HTTPException(status_code=503, detail="TOR connection not available")
    
    result = await darkweb_scraper.scrape(request.dict())
    if result:
        return {"status": "success", "message": "Dark web scraping completed"}
    raise HTTPException(status_code=500, detail="Dark web scraping failed")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)