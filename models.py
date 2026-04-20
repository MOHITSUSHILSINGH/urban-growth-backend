from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class HorizonEnum(str, Enum):
    m12 = "12M"
    m24 = "24M"
    m36 = "36M"
    m48 = "48M"
    m60 = "60M"
    speculative = "Speculative"

class SignalTypeEnum(str, Enum):
    infra = "Infra"
    market = "Market"
    policy = "Policy"
    price = "Price"

class ZoneResponse(BaseModel):
    id: str
    name: str
    city: str
    state: str
    gvs: float
    tags: str
    lat: float
    lng: float
    listing_density: int
    price_per_sqft: int
    rental_yield: float
    appreciation_yoy: float
    undervalued: bool

class HeatmapCell(BaseModel):
    zone: str
    horizon: str
    gvs: float
    driver: str
    color: str

class HeatmapResponse(BaseModel):
    zones: List[str]
    horizons: List[str]
    cells: List[HeatmapCell]

class SignalResponse(BaseModel):
    id: str
    icon: str
    title: str
    source: str
    time_ago: str
    signal_type: str
    zone: str

class IngestionSource(BaseModel):
    source: str
    records: int
    freshness: str
    health_pct: int
    color: str

class PricingDataPoint(BaseModel):
    label: str
    rtm: float
    uc: float

class YieldDataPoint(BaseModel):
    zone: str
    rental_yield: float
    appreciation: float

class KPIResponse(BaseModel):
    active_hot_zones: int
    avg_gvs: float
    municipal_signals: int
    undervalued_zones: int
    hot_zones_delta: int
    gvs_delta: float
