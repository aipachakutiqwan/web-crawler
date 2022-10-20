"""
Output render pydantic class implementation
"""
from pydantic.main import BaseModel


class OutputRenderPayload(BaseModel):
    """
    Output render class implementation
    Args:
        :param BaseModel: BaseModel
    """
    code_audit_process: str
    aam_code: str
    date_received_centera: str
    date_processing: str
    is_full_batch_finished: bool
