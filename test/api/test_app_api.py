"""
Unit tests for class app
"""
import os
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from fastapi import status
from starlette.testclient import TestClient
from src.api.app_api import get_app
from src.api.app_api import APP

app_config_file = os.environ.get('APP_CONFIG_FILE')
log_config_file = os.environ.get('LOG_CONFIG_FILE')

class TestApp(unittest.TestCase):
    """
    Unit tests for class app
    """
    def test_app(self):
        """
        Unit test for app
        :return:
        """
        app = get_app(arg_app_config_file=app_config_file, arg_log_config_file=log_config_file)
        with TestClient(app) as test_client:
            yield test_client

    def test_get_app(self):
        """
        Unit test for get_app method
        :return:
        """
        # plan
        arg_app_config_file = None
        arg_log_config_file = None
        # do
        with\
                patch('src.api.app_api.get_app_config_parameters') as get_app_config_parameters,\
                patch('src.api.app_api.FastAPI') as fast_api,\
                patch('src.api.app_api.configure_logging'),\
                patch('src.api.app_api.start_app_handler') as start_app_handler:
            get_app_config_parameters.return_value = {'app_name': 'name', 'app_version': 1.0,
                                                  'is_debug': False,
                                                   'api_prefix': 'prefix'}
            fast_api.return_value = MagicMock()
            start_app_handler.return_value = None
            fast_app = get_app(arg_app_config_file, arg_log_config_file)
            # check
            self.assertIsNotNone(fast_app)
            self.assertIsInstance(fast_app, MagicMock)
