ZONES_DATA = [
    {"id": "z001", "name": "Aerocity–Dwarka Expressway", "city": "Delhi NCR", "state": "Delhi", "gvs": 91.0, "tags": "Metro + Airport", "lat": 28.5962, "lng": 77.0595, "listing_density": 1840, "price_per_sqft": 8200, "rental_yield": 3.8, "appreciation_yoy": 18.0, "undervalued": False},
    {"id": "z002", "name": "Navi Mumbai Node 5", "city": "Mumbai MMR", "state": "Maharashtra", "gvs": 88.0, "tags": "JNPA Expansion", "lat": 19.0330, "lng": 73.0297, "listing_density": 2210, "price_per_sqft": 7100, "rental_yield": 4.2, "appreciation_yoy": 14.0, "undervalued": False},
    {"id": "z003", "name": "GIFT City Phase 3", "city": "Ahmedabad", "state": "Gujarat", "gvs": 82.0, "tags": "IFSC + SEZ", "lat": 23.1614, "lng": 72.6796, "listing_density": 980, "price_per_sqft": 5800, "rental_yield": 3.1, "appreciation_yoy": 22.0, "undervalued": True},
    {"id": "z004", "name": "Whitefield East", "city": "Bengaluru", "state": "Karnataka", "gvs": 78.0, "tags": "Tech Corridor", "lat": 12.9698, "lng": 77.7499, "listing_density": 3100, "price_per_sqft": 6900, "rental_yield": 4.6, "appreciation_yoy": 12.0, "undervalued": False},
    {"id": "z005", "name": "Hyderabad ORR–Sohna Rd", "city": "Hyderabad", "state": "Telangana", "gvs": 72.0, "tags": "Pharma City", "lat": 17.3616, "lng": 78.4747, "listing_density": 1540, "price_per_sqft": 5200, "rental_yield": 5.1, "appreciation_yoy": 9.0, "undervalued": True},
    {"id": "z006", "name": "Noida Sector 150", "city": "Delhi NCR", "state": "Uttar Pradesh", "gvs": 68.0, "tags": "Expressway Zone", "lat": 28.5274, "lng": 77.3949, "listing_density": 1290, "price_per_sqft": 5600, "rental_yield": 3.4, "appreciation_yoy": 16.0, "undervalued": True},
    {"id": "z007", "name": "Pune Hinjewadi Phase 4", "city": "Pune", "state": "Maharashtra", "gvs": 65.0, "tags": "IT Hub Expansion", "lat": 18.5912, "lng": 73.7383, "listing_density": 2050, "price_per_sqft": 6100, "rental_yield": 4.8, "appreciation_yoy": 11.0, "undervalued": False},
    {"id": "z008", "name": "Chennai OMR South", "city": "Chennai", "state": "Tamil Nadu", "gvs": 61.0, "tags": "Data Centre Cluster", "lat": 12.8231, "lng": 80.2205, "listing_density": 1780, "price_per_sqft": 5400, "rental_yield": 5.3, "appreciation_yoy": 8.0, "undervalued": True},
    {"id": "z009", "name": "Gurugram Sector 84–88", "city": "Delhi NCR", "state": "Haryana", "gvs": 74.0, "tags": "Dwarka Exp Extension", "lat": 28.4089, "lng": 76.9987, "listing_density": 2350, "price_per_sqft": 7400, "rental_yield": 3.6, "appreciation_yoy": 19.0, "undervalued": False},
    {"id": "z010", "name": "Thane Kalyan Node", "city": "Mumbai MMR", "state": "Maharashtra", "gvs": 59.0, "tags": "Trans Harbour Link", "lat": 19.2183, "lng": 73.1769, "listing_density": 3200, "price_per_sqft": 5900, "rental_yield": 4.4, "appreciation_yoy": 10.0, "undervalued": False},
]

HEATMAP_DATA = {
    "zones": ["Aerocity–Dwarka Exp.", "Navi Mumbai Node 5", "Whitefield East BLR", "GIFT City Phase 3", "Hyderabad ORR–Sohna", "Noida Sec 150"],
    "horizons": ["12M", "24M", "36M", "48M", "60M", "Speculative"],
    "cells": [
        {"zone": "Aerocity–Dwarka Exp.", "horizon": "12M", "gvs": 88, "driver": "Metro Ph4", "color": "#085041"},
        {"zone": "Aerocity–Dwarka Exp.", "horizon": "24M", "gvs": 91, "driver": "Metro Ph4", "color": "#085041"},
        {"zone": "Aerocity–Dwarka Exp.", "horizon": "36M", "gvs": 84, "driver": "NMIA Arpt", "color": "#085041"},
        {"zone": "Aerocity–Dwarka Exp.", "horizon": "48M", "gvs": 72, "driver": "SEZ Decl.", "color": "#1D9E75"},
        {"zone": "Aerocity–Dwarka Exp.", "horizon": "60M", "gvs": 65, "driver": "Rapid Rail", "color": "#1D9E75"},
        {"zone": "Aerocity–Dwarka Exp.", "horizon": "Speculative", "gvs": 50, "driver": "Mixed-use", "color": "#EF9F27"},
        {"zone": "Navi Mumbai Node 5", "horizon": "12M", "gvs": 76, "driver": "Trans Harb", "color": "#1D9E75"},
        {"zone": "Navi Mumbai Node 5", "horizon": "24M", "gvs": 80, "driver": "Trans Harb", "color": "#0F6E56"},
        {"zone": "Navi Mumbai Node 5", "horizon": "36M", "gvs": 88, "driver": "JNPA Exp.", "color": "#085041"},
        {"zone": "Navi Mumbai Node 5", "horizon": "48M", "gvs": 92, "driver": "JNPA Exp.", "color": "#085041"},
        {"zone": "Navi Mumbai Node 5", "horizon": "60M", "gvs": 87, "driver": "Port SEZ", "color": "#085041"},
        {"zone": "Navi Mumbai Node 5", "horizon": "Speculative", "gvs": 70, "driver": "Data Ctr", "color": "#1D9E75"},
        {"zone": "Whitefield East BLR", "horizon": "12M", "gvs": 62, "driver": "STRR Road", "color": "#1D9E75"},
        {"zone": "Whitefield East BLR", "horizon": "24M", "gvs": 70, "driver": "Tech Pk", "color": "#1D9E75"},
        {"zone": "Whitefield East BLR", "horizon": "36M", "gvs": 75, "driver": "Tech Pk", "color": "#1D9E75"},
        {"zone": "Whitefield East BLR", "horizon": "48M", "gvs": 80, "driver": "Metro Yell", "color": "#0F6E56"},
        {"zone": "Whitefield East BLR", "horizon": "60M", "gvs": 88, "driver": "Metro Yell", "color": "#085041"},
        {"zone": "Whitefield East BLR", "horizon": "Speculative", "gvs": 79, "driver": "ITR Zone", "color": "#0F6E56"},
        {"zone": "GIFT City Phase 3", "horizon": "12M", "gvs": 55, "driver": "GIFT Ext.", "color": "#EF9F27"},
        {"zone": "GIFT City Phase 3", "horizon": "24M", "gvs": 60, "driver": "GIFT Ext.", "color": "#1D9E75"},
        {"zone": "GIFT City Phase 3", "horizon": "36M", "gvs": 68, "driver": "GIFT Ext.", "color": "#1D9E75"},
        {"zone": "GIFT City Phase 3", "horizon": "48M", "gvs": 74, "driver": "IFSC Exp.", "color": "#1D9E75"},
        {"zone": "GIFT City Phase 3", "horizon": "60M", "gvs": 82, "driver": "IFSC Exp.", "color": "#0F6E56"},
        {"zone": "GIFT City Phase 3", "horizon": "Speculative", "gvs": 91, "driver": "Fintech Hub", "color": "#085041"},
        {"zone": "Hyderabad ORR–Sohna", "horizon": "12M", "gvs": 48, "driver": "ORR NH48", "color": "#EF9F27"},
        {"zone": "Hyderabad ORR–Sohna", "horizon": "24M", "gvs": 55, "driver": "Pharma Cty", "color": "#EF9F27"},
        {"zone": "Hyderabad ORR–Sohna", "horizon": "36M", "gvs": 60, "driver": "Pharma Cty", "color": "#1D9E75"},
        {"zone": "Hyderabad ORR–Sohna", "horizon": "48M", "gvs": 66, "driver": "Pharma Cty", "color": "#1D9E75"},
        {"zone": "Hyderabad ORR–Sohna", "horizon": "60M", "gvs": 72, "driver": "Airport Exp", "color": "#1D9E75"},
        {"zone": "Hyderabad ORR–Sohna", "horizon": "Speculative", "gvs": 80, "driver": "Airport Exp", "color": "#0F6E56"},
        {"zone": "Noida Sec 150", "horizon": "12M", "gvs": 40, "driver": "Exp Wy", "color": "#EF9F27"},
        {"zone": "Noida Sec 150", "horizon": "24M", "gvs": 44, "driver": "Exp Wy", "color": "#EF9F27"},
        {"zone": "Noida Sec 150", "horizon": "36M", "gvs": 50, "driver": "Film City", "color": "#EF9F27"},
        {"zone": "Noida Sec 150", "horizon": "48M", "gvs": 58, "driver": "Film City", "color": "#1D9E75"},
        {"zone": "Noida Sec 150", "horizon": "60M", "gvs": 65, "driver": "Film City", "color": "#1D9E75"},
        {"zone": "Noida Sec 150", "horizon": "Speculative", "gvs": 70, "driver": "Aquifer Z", "color": "#1D9E75"},
    ]
}

SIGNALS_DATA = [
    {"id": "s001", "icon": "🏗", "title": "New metro tender floated — Delhi Phase 4B", "source": "Municipal Corp", "time_ago": "2h ago", "signal_type": "Infra", "zone": "Aerocity–Dwarka Exp."},
    {"id": "s002", "icon": "📈", "title": "Listing density +34% in Navi Mumbai Node 5", "source": "99acres", "time_ago": "4h ago", "signal_type": "Market", "zone": "Navi Mumbai Node 5"},
    {"id": "s003", "icon": "📋", "title": "CLU policy change — Dwarka residential zone expansion", "source": "DDA Gazette", "time_ago": "6h ago", "signal_type": "Policy", "zone": "Aerocity–Dwarka Exp."},
    {"id": "s004", "icon": "🏢", "title": "GIFT IFSC Phase 3 construction commenced", "source": "GIFT City Corp", "time_ago": "1d ago", "signal_type": "Infra", "zone": "GIFT City Phase 3"},
    {"id": "s005", "icon": "📊", "title": "Whitefield RTM prices up 8.2% QoQ", "source": "MagicBricks", "time_ago": "1d ago", "signal_type": "Price", "zone": "Whitefield East BLR"},
    {"id": "s006", "icon": "🚇", "title": "JNPA Phase II tender awarded — ₹4,200 Cr", "source": "Municipal Corp", "time_ago": "2d ago", "signal_type": "Infra", "zone": "Navi Mumbai Node 5"},
    {"id": "s007", "icon": "📉", "title": "Noida Sec 150 under-construction inventory flat for 3rd month", "source": "99acres", "time_ago": "2d ago", "signal_type": "Market", "zone": "Noida Sec 150"},
    {"id": "s008", "icon": "🏛", "title": "RERA approvals up 18% in Hyderabad ORR corridor", "source": "MahaRERA", "time_ago": "3d ago", "signal_type": "Policy", "zone": "Hyderabad ORR–Sohna"},
    {"id": "s009", "icon": "💹", "title": "Gurugram Sector 84 rental absorption hits 91%", "source": "Rental Aggregator", "time_ago": "3d ago", "signal_type": "Market", "zone": "Gurugram Sector 84–88"},
    {"id": "s010", "icon": "🛣", "title": "Pune–Mumbai Hyperloop feasibility study approved", "source": "MoRTH Gazette", "time_ago": "4d ago", "signal_type": "Policy", "zone": "Pune Hinjewadi Phase 4"},
]

INGESTION_DATA = [
    {"source": "Municipal Corp Portals", "records": 148, "freshness": "12 min ago", "health_pct": 94, "color": "#1D9E75"},
    {"source": "99acres / MagicBricks", "records": 8340, "freshness": "28 min ago", "health_pct": 88, "color": "#185FA5"},
    {"source": "DDA / RERA Gazette", "records": 62, "freshness": "1.2 hr ago", "health_pct": 76, "color": "#BA7517"},
    {"source": "Rental Yield Aggregator", "records": 2100, "freshness": "2.4 hr ago", "health_pct": 82, "color": "#534AB7"},
    {"source": "Satellite / OSM Layer", "records": 412, "freshness": "6 hr ago", "health_pct": 70, "color": "#D85A30"},
]

KPI_DATA = {
    "active_hot_zones": 14,
    "avg_gvs": 72.4,
    "municipal_signals": 38,
    "undervalued_zones": 9,
    "hot_zones_delta": 3,
    "gvs_delta": 6.1
}

PRICING_DATA = {
    "12M": [
        {"label": "May", "rtm": 100, "uc": 100},
        {"label": "Jun", "rtm": 103, "uc": 102},
        {"label": "Jul", "rtm": 105, "uc": 103},
        {"label": "Aug", "rtm": 108, "uc": 106},
        {"label": "Sep", "rtm": 112, "uc": 108},
        {"label": "Oct", "rtm": 114, "uc": 110},
        {"label": "Nov", "rtm": 118, "uc": 113},
        {"label": "Dec", "rtm": 121, "uc": 115},
        {"label": "Jan", "rtm": 126, "uc": 118},
        {"label": "Feb", "rtm": 130, "uc": 120},
        {"label": "Mar", "rtm": 134, "uc": 123},
        {"label": "Apr", "rtm": 138, "uc": 126},
    ],
    "24M": [
        {"label": "Apr 24", "rtm": 100, "uc": 100},
        {"label": "Jul 24", "rtm": 104, "uc": 103},
        {"label": "Oct 24", "rtm": 108, "uc": 106},
        {"label": "Jan 25", "rtm": 113, "uc": 109},
        {"label": "Apr 25", "rtm": 118, "uc": 112},
        {"label": "Jul 25", "rtm": 124, "uc": 115},
        {"label": "Oct 25", "rtm": 130, "uc": 118},
        {"label": "Jan 26", "rtm": 135, "uc": 121},
        {"label": "Apr 26", "rtm": 141, "uc": 124},
    ],
    "60M": [
        {"label": "2022", "rtm": 100, "uc": 100},
        {"label": "2023", "rtm": 108, "uc": 106},
        {"label": "2024", "rtm": 119, "uc": 113},
        {"label": "2025", "rtm": 132, "uc": 121},
        {"label": "2026E", "rtm": 148, "uc": 130},
        {"label": "2027E", "rtm": 168, "uc": 140},
        {"label": "2028E", "rtm": 191, "uc": 151},
        {"label": "2029E", "rtm": 215, "uc": 163},
    ]
}

YIELD_DATA = [
    {"zone": "Aerocity", "rental_yield": 3.8, "appreciation": 18.0},
    {"zone": "Navi Mum", "rental_yield": 4.2, "appreciation": 14.0},
    {"zone": "GIFT City", "rental_yield": 3.1, "appreciation": 22.0},
    {"zone": "Whitefld", "rental_yield": 4.6, "appreciation": 12.0},
    {"zone": "Hyd ORR", "rental_yield": 5.1, "appreciation": 9.0},
    {"zone": "Noida 150", "rental_yield": 3.4, "appreciation": 16.0},
    {"zone": "Gurugram", "rental_yield": 3.6, "appreciation": 19.0},
    {"zone": "Thane", "rental_yield": 4.4, "appreciation": 10.0},
    {"zone": "Pune HW", "rental_yield": 4.8, "appreciation": 11.0},
    {"zone": "Chennai OMR", "rental_yield": 5.3, "appreciation": 8.0},
]
