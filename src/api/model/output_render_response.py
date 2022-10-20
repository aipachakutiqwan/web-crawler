"""
Output render response pydantic class implementation
"""
from pydantic import BaseModel


class OutputRenderResponse(BaseModel):
    """
    Output render response pydantic class implementation
    Args:
        :param BaseModel: BaseModel
    """
    result: str
