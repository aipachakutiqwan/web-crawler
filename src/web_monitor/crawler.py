import asyncio
import sched
import aiohttp
import time
import ssl
import certifi
import logging
from src.model.response_log import ResponseLog
from datetime import datetime

class Crawler():

    def __init__(self, config_app: dict, list_webs: list, checking_period_seconds: float ) -> None:
        self.config_app = config_app
        self.list_webs = list_webs
        self.checking_period_seconds = checking_period_seconds
        self.crawler_scheduler = sched.scheduler(time.time, time.sleep)
        self.timeout = 60

    async def async_get(self, url, session, sslcontext, requirement_content):
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


    async def async_request(self, url, session, sslcontext):
        async with session.request('GET', url=url, ssl=sslcontext) as response:
            return await response.text(), response.status, url


    async def bound_semaphore(self, semaphore, web, session, sslcontext, requirement_content):
        async with semaphore:
            return await self.async_get(web, session, sslcontext, requirement_content)


    async def call_web_pages(self, list_webs: list):
        logging.info(f"Starting new checking period: {datetime.now()}")
        start_time_call_web_pages = time.time()
        semaphore = asyncio.Semaphore(len(list_webs))
        sslcontext = ssl.create_default_context(cafile=certifi.where())
        client_timeout = aiohttp.ClientTimeout(total=self.timeout)
        array_logs = []
        async with aiohttp.ClientSession(timeout=client_timeout) as session:
            tasks = []
            for url, requirement_content in list_webs:
                #tasks.append(asyncio.create_task(session.get(url)))
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
        self.crawler_scheduler.enter(self.checking_period_seconds, 1,
                                     self.run_job,
                                     argument=([self.list_webs]))

    def run_job(self, list_webs: list) -> None:
        asyncio.run(self.call_web_pages(list_webs))
        self.enter_scheduler()

    def schedule_job(self) -> None:
        self.crawler_scheduler.enter(self.checking_period_seconds, 1,
                                     self.run_job,
                                     argument=([self.list_webs]))
        self.crawler_scheduler.run()
