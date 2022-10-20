"""
Unit Tests - Core Config
"""
import unittest
from unittest.mock import MagicMock, patch, mock_open
import yaml
from src.log_manager.config import get_app_config_parameters


class TestConfig(unittest.TestCase):
    """ Test Class - api/core/config """

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    @patch("src.log_manager.config.yaml.safe_load", return_value={})
    def test_get_app_config_parameters(self, mock_yaml, mock_file):
        """ Test get_app_config_parameters() """
        test_app_config_file = "path/to/open"
        self.assertEqual(open(test_app_config_file, encoding='utf8').read(), "data")
        self.assertDictEqual(get_app_config_parameters(MagicMock()), {})

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    @patch("src.log_manager.config.yaml.safe_load", side_effect=yaml.YAMLError)
    def test_get_app_config_parameters_safe_load_exception(self, mock_yaml, mock_file):
        """ Test get_app_config_parameters() """
        test_app_config_file = "path/to/open"
        self.assertEqual(open(test_app_config_file, encoding='utf8').read(), "data")
        self.assertRaises(RuntimeError, get_app_config_parameters, test_app_config_file)

    @patch("builtins.open", new_callable=mock_open, read_data="data")
    def test_get_app_config_parameters_open_exception(self, mock_file):
        """ Test get_app_config_parameters() """
        mock_file.side_effect = Exception
        test_app_config_file = "path/to/open"
        self.assertRaises(RuntimeError, get_app_config_parameters, test_app_config_file)

if __name__ == "__main__":
    unittest.main()
