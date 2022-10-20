"""
Output handler implementation
"""
import logging
from fastapi import APIRouter
from starlette.requests import Request
from src.api.model.monitoring_payload import MonitoringPayload
from src.api.model.monitoring_response import MonitoringResponse

ROUTER = APIRouter()


@ROUTER.post("/america", response_model=MonitoringResponse)
async def get_monitoring_america_pages(monitoring_payload: MonitoringPayload,
                           request: Request) -> MonitoringResponse:
    """
    :param monitoring_payload:
    :param request: request containing handlers
    """
    distribuited_monitoring: DistribuitedMonitoring = request.app.state.distribuited_monitoring
    result = "OK"
    try:
        logs = distribuited_monitoring.monitor_webpages(monitoring_payload)
    except Exception as ex:
        logging.error(f"MONITORING_ERROR: {ex} ")
        result = "KO"
    return MonitoringResponse(result=logs)
