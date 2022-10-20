"""
Start up the handler class
"""
import logging
from typing import Callable
from fastapi import FastAPI
from src.handlers.output_render_handler import OutputRenderHandler
from src.handlers.output_render_retry_handler import OutputRenderRetryHandler


def _startup_model(app: FastAPI, app_config: dict) -> None:
    output_render_handler = OutputRenderHandler(app_config)
    output_render_retry_handler= OutputRenderRetryHandler(app_config)
    app.state.output_render_handler = output_render_handler
    app.state.output_render_retry_handler = output_render_retry_handler
    logging.info("Request handler initialized")


def start_app_handler(app: FastAPI, app_config: dict) -> Callable:
    """
     Start up the handler class and set it in the FastAPI config.

     Args:
         :param app: FastAPI class

     Returns:
         FastAPI configured
     """
    def startup() -> None:
        logging.info("Running app start handler.")
        _startup_model(app, app_config)

    return startup
