"""
Script to start up front end web monitoring.
"""
import asyncio
import argparse
from flask import Flask
from flask import request
from src.web_monitor.crawler import Crawler
from src.utils.utils import read_file

app = Flask(__name__)
PATH_WEB_FILES = './config/webs.txt'
list_webs = read_file(PATH_WEB_FILES)
CHECKING_PERIOD_SECONDS = 1

@app.route("/")
async def index():
    """
    Show a form in front end to request web crawler monitoring
    Args:
        :param
    Returns:
        response: web log monitoring in front end.
    """
    monitoring = request.args.get("monitoring", "")
    if monitoring:
        crawler = Crawler({}, list_webs, CHECKING_PERIOD_SECONDS)
        tasks = []
        tasks.append(asyncio.create_task(crawler.call_web_pages(list_webs)))
        list_logs = await asyncio.gather(*tasks)
        logs = ""
        for log_web in list_logs[0]:
            logs = logs + str(log_web) + "<br>"
    else:
        logs = "Please click botton"
    return (
        """<form action="" method="get">
                <input type="submit" value="Run web crawler" name="monitoring">
            </form>"""
        + "List logs: <br> <br>"
        + logs
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="set port", required=True)
    args = parser.parse_args()
    app.run(host="127.0.0.1", port=int(args.port), debug=True)
