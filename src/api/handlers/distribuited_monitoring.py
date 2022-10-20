"""
DistribuitedMonitoring class for monitor web pages in America
"""
import ssl
import asyncio
import aiohttp
import certifi
from src.api.model.monitoring_payload import MonitoringPayload
from src.web_monitor.crawler import Crawler


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
        self.checking_period_seconds = 1
        self.session = aiohttp.ClientSession()
        self.sslcontext = ssl.create_default_context(cafile=certifi.where())

    async def monitor_webpages(self, monitoring_payload: MonitoringPayload):
        """
        Monitor a list of web pages in America
        Args:
            :param monitoring_payload: pydantic class with list of webpages to monitor
        Returns:
            response:
        """
        list_webs = monitoring_payload.list_webs
        crawler = Crawler({}, list_webs, self.checking_period_seconds)
        tasks = []
        tasks.append(asyncio.create_task(crawler.call_web_pages(list_webs)))
        list_logs = await asyncio.gather(*tasks)
        return list_logs[0]
