# Urban Growth Engine — Backend API

FastAPI backend providing the Predictive Urban Growth Analytics Engine.

## Setup

```bash
pip install -r requirements.txt
python main.py
```

API runs at: http://localhost:8000
Swagger docs: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /api/zones | List all growth zones (filterable) |
| GET | /api/zones/{id} | Zone detail |
| GET | /api/zones/{id}/analysis | Deep zone analysis + risk factors |
| GET | /api/heatmap | Full GVS heatmap matrix |
| GET | /api/heatmap/gvs-algorithm | GVS algorithm weights/formula |
| GET | /api/signals | Live signal feed |
| GET | /api/signals/summary | Signal type breakdown |
| GET | /api/analytics/kpis | Dashboard KPIs |
| GET | /api/analytics/yield-gap | Rental yield vs appreciation data |
| GET | /api/analytics/pricing-velocity | RTM vs UC pricing trends |
| GET | /api/analytics/market-overview | Market summary |
| GET | /api/analytics/correlation-matrix | Indicator correlation matrix |
| GET | /api/ingestion/status | Data source ingestion health |
| GET | /api/ingestion/sources | Source catalog |
| POST | /api/ingestion/trigger-refresh | Manual data refresh |

## Architecture

```
backend/
├── main.py              # FastAPI app + CORS setup
├── models.py            # Pydantic schemas
├── requirements.txt
├── routers/
│   ├── zones.py         # Zone CRUD + analysis
│   ├── signals.py       # Live signal feed
│   ├── heatmap.py       # GVS heatmap data
│   ├── analytics.py     # KPIs, pricing, yield
│   └── ingestion.py     # Data source status
└── data/
    └── mock_data.py     # Seed data (replace with DB/scrapers)
```

## GVS Algorithm Weights

| Indicator | Weight |
|-----------|--------|
| Municipal Declarations | 35% |
| Listing Density Trend | 20% |
| Pricing Velocity | 20% |
| Rental Absorption | 15% |
| Zoning Policy Signals | 10% |
