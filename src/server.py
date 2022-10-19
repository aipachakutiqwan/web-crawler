from flask import Flask
import asyncio
import aiohttp
import ssl
import certifi
from src.core.crawler import Crawler
from src.utils.utils import read_file
app = Flask(__name__)

path_web_files = './config/webs.txt'
list_webs = read_file(path_web_files)
checking_period_seconds = 1

@app.route('/')
async def index():
    CWL = Crawler({}, list_webs, checking_period_seconds)
    tasks = []
    tasks.append(asyncio.create_task(CWL.call_web_pages(list_webs)))
    list_logs = await asyncio.gather(*tasks)
    return list_logs[0]

if __name__ == "__main__":
    app.run('localhost', 5009, debug=True)
