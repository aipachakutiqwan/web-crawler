""""
Unit Tests - Crawler class
"""
import os
import unittest
import aiohttp
import ssl
import certifi
import asyncio
from src.log_manager.config import get_app_config_parameters
from src.log_manager.log_management import configure_logging
from src.core.crawler import Crawler
from src.utils.utils import read_file

class TestCrawler(unittest.TestCase):
    """ Test Class - Crawler """

    def setUp(self):
        """ Set up initial class variables """
        app_config_file = os.environ.get('APP_CONFIG_FILE', './config/app_config.yaml')
        log_config_file = os.environ.get('LOG_CONFIG_FILE', './config/log_config.yaml')
        self.config = get_app_config_parameters(app_config_file)
        log_config = get_app_config_parameters(log_config_file)
        configure_logging(self.config, log_config)
        path_web_files = './config/webs.txt'
        self.list_webs = read_file(path_web_files)
        self.session = aiohttp.ClientSession()
        self.sslcontext = ssl.create_default_context(cafile=certifi.where())

    def test_async_request_200(self):
        """ Test 200 OK response """
        CWL = Crawler(self.config, self.list_webs, 1)
        url = 'https://httpbin.org'
        requirement_content = 'simple HTTP Request'
        task = CWL.async_get(url, self.session, self.sslcontext, requirement_content)
        loop = asyncio.get_event_loop()
        future = loop.run_until_complete(task)
        assert future['status']==200

    def test_async_request_404(self):
        """ Test 404 Not Found response """
        CWL = Crawler(self.config, self.list_webs, 1)
        url = 'https://httpbin.org/notfound'
        requirement_content = 'simple HTTP Request'
        task = CWL.async_get(url, self.session, self.sslcontext, requirement_content)
        loop = asyncio.get_event_loop()
        future = loop.run_until_complete(task)
        assert future['status']==404

    def test_async_request_ssl(self):
        """ Test ssl connection boolean """
        CWL = Crawler(self.config, self.list_webs, 1)
        url = 'https://python.org'
        requirement_content = 'Python is a programming language that lets you work quickly'
        sslcontext = False
        task = CWL.async_get(url, self.session, sslcontext, requirement_content)
        loop = asyncio.get_event_loop()
        future = loop.run_until_complete(task)
        assert future['status']==200

