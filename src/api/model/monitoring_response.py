"""
MonitoringResponse pydantic class implementation
"""
from pydantic import BaseModel


class MonitoringResponse(BaseModel):
    """
    MonitoringResponse pydantic class implementation
    Args:
        :param BaseModel: BaseModel
    """
    result: list
