"""
Test monitoring call api rest
"""
import requests
import os

def test_monitoring():
    """
    Test monitoring call api
    """
    payload = {
        "datetime_monitoring": "today"
    }
    url = "http://localhost:9083/api/monitoring/america"
    response = requests.post(url,
                             json=payload,
                             proxies={"http":"", "https":""},
                             verify=False
                             )
    print(response.text)
    assert response.status_code == 200
test_monitoring()