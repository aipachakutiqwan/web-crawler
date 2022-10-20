"""
MonitoringPayload pydantic class implementation
"""
from pydantic.main import BaseModel


class MonitoringPayload(BaseModel):
    """
    MonitoringPayload class implementation
    Args:
        :param BaseModel: BaseModel
    """
    datetime_monitoring: str
