"""
MonitoringResponse pydantic class implementation
"""
from typing import List
from pydantic import BaseModel

class MonitoringResponse(BaseModel):
    """
    MonitoringResponse pydantic class implementation
    Args:
        :param BaseModel: BaseModel
    """
    response: List
