"""
Unit test for heartbeat
"""
import unittest
from unittest.mock import patch
from src.api.router import heartbeat

class TestHeartbeat(unittest.TestCase):
    """
    Unit test for heartbeat
    """
    def test_get_heartbeat(self):
        """
        Unit test for get_heartbeat method
        :return:
        """
        with \
            patch('src.api.router.heartbeat.HeartbeatResponse') as \
                    HeartbeatResponse:
            HeartbeatResponse.return_value = True
            heartbeat_response = heartbeat.get_heartbeat()
            # check
            assert heartbeat_response
