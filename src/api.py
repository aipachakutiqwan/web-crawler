import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.api.app_api:APP", host="0.0.0.0", port=9083, log_level="info")
