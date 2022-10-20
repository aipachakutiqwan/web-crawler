"""
Main script for console web monitoring logs,
output logs will be also writting in ./logs folder

"""
import os
import argparse
from src.log_manager.config import get_app_config_parameters
from src.log_manager.log_management import configure_logging
from src.web_monitor.crawler import Crawler
from src.utils.utils import read_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--checking_period_seconds",
                        help="checking_period_seconds", required=True)
    args = parser.parse_args()
    app_config_file = os.environ.get('APP_CONFIG_FILE', './config/app_config.yaml')
    log_config_file = os.environ.get('LOG_CONFIG_FILE', './config/log_config.yaml')
    config = get_app_config_parameters(app_config_file)
    log_config = get_app_config_parameters(log_config_file)
    configure_logging(config, log_config)
    PATH_WEB_FILES = './config/webs.txt'
    list_webs = read_file(PATH_WEB_FILES)
    checking_period_seconds = float(args.checking_period_seconds)
    crawler = Crawler(config, list_webs, checking_period_seconds)
    crawler.schedule_job()
