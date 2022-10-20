"""
Test monitoring call api rest
"""
import requests
import os

def test_monitoring():
    """
    Test API call which monitor a list of webservices (web page, content requirement)
    """
    payload = {
        "list_webs":
            [
                ("https://httpbin.org","simple HTTP Request"),
                ("https://example.org","This domain is for use in illustrative examples in documents."),
                ("https://reddit.com","app_html_start"),
                ("https://python.org","Python is a programming language that lets you work quickly")
             ]
    }
    url = "http://localhost:8082/api/monitoring/america"
    response = requests.post(url,
                             json=payload,
                             proxies={"http":"", "https":""},
                             verify=False
                             )
    print(response.text)
    assert response.status_code == 200
test_monitoring()