"""
Output handler implementation
"""
import logging
import os
from time import sleep
from fastapi import APIRouter, Depends
from starlette.background import BackgroundTasks
from starlette.requests import Request
from src.api.core.security import is_authenticated
from src.api.model.output_render_payload import OutputRenderPayload
from src.api.model.output_render_response import OutputRenderResponse
from src.handlers.output_render_handler import OutputRenderHandler
from src.utils.log_message import base_log_message

ROUTER = APIRouter()


def do_get_final_result(output_render_payload: OutputRenderPayload,
                        output_render_handler: OutputRenderHandler,
                        base_log):
    """
    Process results for the specific audit process
    Args:
        :param output_render_payload:
        :param output_render_Handler:
        :param base_log:
    Returns:
        response:
    """

    try:
        logging.info(f"Request received from document uploader: {base_log}")
        sleep_time = int(os.environ.get('INITIAL_SLEEP_TIME', '5'))
        logging.info(f"Call received, sleeping {sleep_time} seconds: {base_log}")
        sleep(sleep_time)
        logging.info(f"Checking documents in redis: {base_log}")
        output_render_handler.process_list_documents(
            output_render_payload=output_render_payload)
    except Exception as ex:
        logging.error(f"OUTPUT_HANDLER_ERROR: {ex} : {base_log}")


@ROUTER.post("/final-result", response_model=OutputRenderResponse)
async def get_final_result(output_render_payload: OutputRenderPayload,
                           request: Request,
                           background_tasks: BackgroundTasks,
                           _=Depends(is_authenticated)) -> OutputRenderResponse:
    """
    :param _:
    :param output_render_payload:
    :param request: request containing handlers
    :param background_tasks: needed for async execution
    """
    base_log = base_log_message(output_render_payload)
    output_render_handler: OutputRenderHandler = request.app.state.output_render_handler
    result = "OK"
    try:
        background_tasks.add_task(do_get_final_result,
                                  output_render_payload,
                                  output_render_handler,
                                  base_log)
    except Exception as ex:
        logging.error(f"OUTPUT_HANDLER_ERROR: {ex} : {base_log}")
        result = "KO"
    return OutputRenderResponse(result=result)
