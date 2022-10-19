from flask import Flask
from flask import request
import asyncio
from src.core.crawler import Crawler
from src.utils.utils import read_file

app = Flask(__name__)
print(f"start reading")
path_web_files = './config/webs.txt'
list_webs = read_file(path_web_files)
checking_period_seconds = 1
print(f"end reading")

@app.route("/")
async def index():
    monitoring = request.args.get("monitoring", "")
    if monitoring:
        CWL = Crawler({}, list_webs, checking_period_seconds)
        tasks = []
        tasks.append(asyncio.create_task(CWL.call_web_pages(list_webs)))
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
    app.run(host="127.0.0.1", port=5020, debug=True)