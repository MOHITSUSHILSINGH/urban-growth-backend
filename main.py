from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from routers import zones, signals, heatmap, analytics, ingestion

app = FastAPI(
    title="Predictive Urban Growth Engine API",
    description="Geospatial analytics engine for real estate investment hotspot identification",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(zones.router, prefix="/api/zones", tags=["Zones"])
app.include_router(signals.router, prefix="/api/signals", tags=["Signals"])
app.include_router(heatmap.router, prefix="/api/heatmap", tags=["Heatmap"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(ingestion.router, prefix="/api/ingestion", tags=["Ingestion"])

@app.get("/")
def root():
    return {"message": "Predictive Urban Growth Engine API", "version": "1.0.0", "status": "running"}

@app.get("/api/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
