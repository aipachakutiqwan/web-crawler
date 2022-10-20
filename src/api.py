"""
Script to start up the API client webservices in multiple
geographically distributed locations.

"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.api.app_api:APP", host="0.0.0.0", port=8082, log_level="info")
