"""
Unit test for log management class
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from src.log_manager import log_management


class TestLogManagement(unittest.TestCase):
    """
    Unit test for log management class
    """
    def test_configure_logging(self):
        """
        Unit test for configure_logging method
        :return:
        """
        # plan
        config = {'work_dir': None}
        log_config = {'TEST': None}
        # do
        with\
                patch('src.log_manager.log_management.os.path') as os_path,\
                patch('src.log_manager.log_management.logging.config') as logging_config,\
                patch('src.log_manager.log_management.os.makedirs') as os_makedirs:
            os_path.return_value = None
            os_path.join = MagicMock(return_value=None)
            log_management.configure_logging(config, log_config)
            # check
            logging_config.dictConfig.assert_called_once_with(log_config)
            os_makedirs.assert_called_once_with(None, exist_ok=True)

    def test_filter(self):
        """
        Unit test for filter method
        :return:
        """
        with self.subTest():
            # plan
            record = MagicMock()
            # do
            target = log_management.CorrIdFilter()
            filter_flag = target.filter(record)
            # check
            self.assertEqual(record.corrId, 'no-corr')

        with self.subTest():
            # plan
            corr = 12345
            # do
            record.args = {'corrId': corr}
            target = log_management.CorrIdFilter()
            filter_flag = target.filter(record)
            # check
            self.assertEqual(record.corrId, corr)
