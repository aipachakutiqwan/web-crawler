"""
MonitoringResponse pydantic class implementation
"""
from pydantic import BaseModel
from typing import List, Optional


class MonitoringResponse(BaseModel):
    """
    MonitoringResponse pydantic class implementation
    Args:
        :param BaseModel: BaseModel
    """
    response: List
