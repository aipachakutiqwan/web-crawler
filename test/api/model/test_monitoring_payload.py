"""
Unit tests for pydantic monitoring_payload class
"""
import unittest
from pydantic.main import BaseModel
from src.api.model import monitoring_payload


class TestMonitoringPayload(unittest.TestCase):
    """
    Unit tests for monitoring_payload class
    """
    def setUp(self):
        """
        Set configuration
        """
        self.list_webs = [
                ("https://httpbin.org","simple HTTP Request"),
                ("https://example.org","This domain is for use in illustrative examples in documents."),
                ("https://reddit.com","app_html_start"),
                ("https://python.org","Python is a programming language that lets you work quickly")
             ]

    def test_TestMonitoring(self):
        """
        Unit test for monitoring_payload class
        :return:
        """
        # do
        target = monitoring_payload.MonitoringPayload(
            list_webs=self.list_webs
        )
        # check
        assert isinstance(target, BaseModel)