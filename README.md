# Web Monitoring (Crawler)

## Overview
This repository implements an online monitoring of web pages according to a parameterized checking period. 
The application parallelize the request to the webpages using concurrently coroutines with semaphore to have better control over their executions. 
This IO-bound application uses mainly built-in python packages, asyncio for concurrent async web request and sched for schedule periodic monitoring.
In addition offer a simple web interface for application monitoring.

## Structure

TBD

## Installation

After creation of proper virtual environment for python 3.10.4.
Run installation setup script with the following command.

```console
pip install .
```

## How to run the application

The console application will start up with the next command, set desired value for checking_period_seconds. 
```console
python3 src/main_app.py --checking_period_seconds 1
```

The web server will start up with the next command, it is possible to set proper port. 

```console
python3 src/server.py --port 5000
```
After the server is running open the browser on the defined port: http://localhost:5000 and click on "Run web crawler" botton to see the logs.

## How to run test cases

If you would like to run some unit tests.

```console
pytest test
```

