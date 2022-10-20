"""
Concurrently asynchronous web pages monitoring.
It is used to create the console (file output),
front end and API client microservice web crawler monitoring.
"""

import asyncio
import sched
import aiohttp
import time
import ssl
import certifi
import logging
from src.utils.response_log import ResponseLog
from datetime import datetime

class Crawler():
    """
    Asynchronous web pages crawler monitoring
    """

    def __init__(self, config_app: dict, list_webs: list, checking_period_seconds: float ) -> None:
        """
        Initialize required crawler application parameters.
        Args:
            :param  config_app: application configuration parameters
            :param  list_webs: Tuple list of urls to monitor with their content requirement
            :param  checking_period_seconds: Checking monitoring crawler period in seconds.
        """
        self.config_app = config_app
        self.list_webs = list_webs
        self.checking_period_seconds = checking_period_seconds
        self.crawler_scheduler = sched.scheduler(time.time, time.sleep)
        self.timeout = 60

    async def async_get(self, url, session, sslcontext, requirement_content):
        """
        Async GET request to the specified URL. It verifies text requirement content
        ONLY if it received successful response (200),
        other response codes are indicated in the log response.
        Scheduler are reestablished in case error occurs during monitoring (e.g. timeout)
        Args:
            :param  url: url to be monitored
            :param  session: opened shared client session
            :param  sslcontext: ssl certificate context for secure web monitoring connections
            :param  requirement_content: string url content requirement
        Returns:
            Web log monitoring results for the specific URL
        """
        response_log = None
        try:
            async with session.get(url, ssl=sslcontext) as response:
                start_time = time.time()
                response_text = await response.text()
                end_time = time.time()
                response_time = end_time - start_time
                if response.status==200:
                    content_verification = \
                        "CORRECT_CONTENT" if requirement_content in response_text else "INCORRECT_CONTENT"
                else:
                    content_verification = ""
                response_log = ResponseLog(url=url, status=response.status, response_time=response_time,
                                  content_verification=content_verification)
                logging.info(f"{response_log}")

        except Exception as ex:
            logging.debug(f"Error request {url}: {ex}")
            response_log = ResponseLog(url=url, status=None, response_time=None,
                                       content_verification="timeout")
            logging.info(response_log)
            self.enter_scheduler()
        return response_log.dict()



    async def bound_semaphore(self, semaphore, url, session, sslcontext, requirement_content):
        """
        Async semaphore bounded which manages an internal counter, it is decremented by each acquire call
        and incremented by each release call; when acquire finds that it is zero,
        it blocks, waiting until some task calls release.
        Args:
            :param  semaphore: semaphore internal bounded counter
            :param  url: url to be monitored
            :param  session: opened shared client session
            :param  sslcontext: ssl certificate context for secure web monitoring connections
            :param  requirement_content: string url content requirement
        Returns:
            Semaphore bounded async function.
        """
        async with semaphore:
            return await self.async_get(url, session, sslcontext, requirement_content)


    async def call_web_pages(self, list_webs: list):
        """
        Create asynchronously independent url monitoring tasks with a shared client session and
        render asynchronous finished task, using a proper semaphore
        Args:
            :param  list_webs: list urls with their content requirement
        Returns:
            Monitoring logs for every provided url.
        """
        logging.info(f"Starting new checking period: {datetime.now()}")
        start_time_call_web_pages = time.time()
        semaphore = asyncio.Semaphore(len(list_webs))
        sslcontext = ssl.create_default_context(cafile=certifi.where())
        client_timeout = aiohttp.ClientTimeout(total=self.timeout)
        array_logs = []
        async with aiohttp.ClientSession(timeout=client_timeout) as session:
            tasks = []
            for url, requirement_content in list_webs:
                start = time.time()
                logging.debug(f"Start time url: {url}: {start}")
                tasks.append(asyncio.create_task(self.bound_semaphore(semaphore, url,
                                                                      session, sslcontext,
                                                                      requirement_content)))
            list_logs = await asyncio.gather(*tasks)
            for log in list_logs:
                logging.debug(f"log: {log}")
                array_logs.append(log)
        end_time_call_web_pages = time.time()
        logging.info(f"Total time processed the whole request: "
                     f"{end_time_call_web_pages - start_time_call_web_pages }")
        return array_logs

    def enter_scheduler(self):
        """
        Create enter scheduler for asynchronously webs monitoring
        """
        self.crawler_scheduler.enter(self.checking_period_seconds, 1,
                                     self.run_job,
                                     argument=([self.list_webs]))

    def run_job(self, list_webs: list) -> None:
        """
        Run webs monitoring asynchronously and concurrently using asyncio library
        Args:
            :param  list_webs: list urls with their content requirement
        Returns:
            Enter concurrently webs monitoring
        """
        asyncio.run(self.call_web_pages(list_webs))
        self.enter_scheduler()

    def schedule_job(self) -> None:
        """
        Start up the monitoring scheduler calling to
        the web crawler self.run_job callback function
        Args:
            :param
        Returns:
            started scheduler
        """
        self.crawler_scheduler.enter(self.checking_period_seconds, 1,
                                     self.run_job,
                                     argument=([self.list_webs]))
        self.crawler_scheduler.run()
