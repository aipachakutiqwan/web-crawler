"""
Webservices routers definition
"""
from fastapi import APIRouter
from src.api.router import heartbeat
from src.api.router import output_render
from src.api.router import redis
from src.api.router import output_render_retry

API_ROUTER = APIRouter()

API_ROUTER.include_router(heartbeat.ROUTER, tags=["Heartbeat"], prefix="/heartbeat")
API_ROUTER.include_router(output_render.ROUTER, tags=["Output Render Handler"], prefix="/output-render")
API_ROUTER.include_router(output_render_retry.ROUTER, tags=["Output Render Retry Handler"], prefix="/output-render")
API_ROUTER.include_router(redis.ROUTER, tags=["Redis"], prefix="/redis")
