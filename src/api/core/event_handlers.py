"""
Start up the handler class
"""
import logging
from typing import Callable
from fastapi import FastAPI
from src.api.handlers.distribuited_monitoring import DistribuitedMonitoring


def _startup_model(app: FastAPI, app_config: dict) -> None:
    """
     Start up API.
     Args:
         :param app: FastAPI class
         :param app_config: application config
     Returns:
         Set API FastAPI
     """
    distribuited_monitoring = DistribuitedMonitoring(app_config)
    app.state.distribuited_monitoring = distribuited_monitoring
    logging.info("Request handler initialized")


def start_app_handler(app: FastAPI, app_config: dict) -> Callable:
    """
     Start up the handler class and set it in the FastAPI config.
     Args:
         :param app: FastAPI class
         :param app_config: application config
     Returns:
         FastAPI configured
     """
    def startup() -> None:
        logging.info("Running app start handler.")
        _startup_model(app, app_config)
    return startup
