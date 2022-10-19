"""
Main script and module entrypoint
"""
import os
from src.log_manager.config import get_app_config_parameters
from src.log_manager.log_management import configure_logging
from src.core.crawler import Crawler
from src.utils.utils import read_file

if __name__ == "__main__":
    app_config_file = os.environ.get('APP_CONFIG_FILE', './config/app_config.yaml')
    log_config_file = os.environ.get('LOG_CONFIG_FILE', './config/log_config.yaml')
    config = get_app_config_parameters(app_config_file)
    log_config = get_app_config_parameters(log_config_file)
    configure_logging(config, log_config)
    path_web_files = './config/webs.txt'
    list_webs = read_file(path_web_files)
    checking_period_seconds = 1
    crawler = Crawler(config, list_webs, checking_period_seconds)
    crawler.schedule_job()