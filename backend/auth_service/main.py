from fastapi import FastAPI
from .uaepass_auth import router

app = FastAPI(title="SOCMINT UAE PASS Authentication Service")

# Include the UAE PASS router
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
