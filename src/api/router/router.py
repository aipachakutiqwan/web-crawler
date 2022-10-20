"""
Webservices routers definition
"""
from fastapi import APIRouter
from src.api.router import heartbeat
from src.api.router import monitoring
API_ROUTER = APIRouter()
API_ROUTER.include_router(heartbeat.ROUTER, tags=["Heartbeat"], prefix="/heartbeat")
API_ROUTER.include_router(monitoring.ROUTER, tags=["Monitoring"], prefix="/monitoring")
