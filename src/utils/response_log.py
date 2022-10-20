"""
ResponseLog pydantic class implementation
"""
from typing import Optional
from pydantic.main import BaseModel

class ResponseLog(BaseModel):
    """
    ResponseLog pydantic class implementation
    Args:
        :param BaseModel: BaseModel
    """
    url: str
    status: Optional[int]
    response_time: Optional[float]
    content_verification: str

    def log_str(self) -> str:
        """
        Function to string log from ResponseLog.
        Args:
            :param
        Returns:
            log
        """
        str_log = self.url + ' ' + str(self.status) + ' ' + \
                  str(self.response_time) + ' ' + \
                  str(self.content_verification)

        return str_log

