"""
DistribuitedMonitoring class for monitor web pages in America
"""
import json
import logging
import asyncio
from src.api.model.monitoring_payload import MonitoringPayload
from src.web_monitor.crawler import Crawler
from src.utils.utils import read_file


class DistribuitedMonitoring():
    """
    DistribuitedMonitoring class for monitor web pages in America
    """
    def __init__(self, app_config):
        """
        Initialize variables
        Args:
            :param
        Returns:
            response:
        """
        self.app_config =  app_config
        self.path_web_files = './config/webs.txt' #TODO: obtain from env
        self.list_webs = read_file(self.path_web_files)
        self.checking_period_seconds = 1


    async def monitor_webpages(self, monitoring_payload: MonitoringPayload):
        """
        Monitor a list of web pages in America
        Args:
            :param monitoring_payload:
        Returns:
            response:
        # """

        CWL = Crawler({}, self.list_webs, self.checking_period_seconds)
        tasks = []
        tasks.append(asyncio.create_task(CWL.call_web_pages(self.list_webs)))
        list_logs = await asyncio.gather(*tasks)
        logs = []
        for log_web in list_logs[0]:
            logs.append(log_web)
        logging.info(f"logs: {logs}")
        return list_logs
