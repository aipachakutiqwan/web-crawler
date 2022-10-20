"""
Unit test for event handler class
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from src.api.core import event_handlers

class TestEventHandlers(unittest.TestCase):
    """
    Unit test for event handler class
    """
    def test_startup_model(self):
        """
        Unit test for startup_model method
        :return:
        """
        # plan
        app = MagicMock()
        app_config = {}
        # do
        with \
                patch('src.api.core.event_handlers.DistribuitedMonitoring') as distribuited_monitoring,\
                patch('src.api.core.event_handlers.logging.info') as logging_info:
            distribuited_monitoring.return_value = 'TEST'
            event_handlers._startup_model(app, app_config)
            # check
            #assert app.state.model == 'TEST'
            logging_info.assert_called_once_with('Request handler initialized')

    def test_start_app_handler(self):
        """
        Unit test for start_app_handler method
        :return:
        """
        # plan
        app = 'TEST'
        app_config = {}
        # do
        with\
                patch('src.api.core.event_handlers.logging.info') as logging_info,\
                patch('src.api.core.event_handlers._startup_model') as startup_model:

            startup = event_handlers.start_app_handler(app, app_config)
            startup()
            # check
            self.assertTrue(startup)
            logging_info.assert_called_once_with('Running app start handler.')
            startup_model.assert_called_once_with(app, app_config)
