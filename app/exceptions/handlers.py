import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.base import AppException

logger = logging.getLogger(__name__)


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.message, "path": request.url.path},
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unexpected error while processing %s", request.url.path)
    return JSONResponse(status_code=500, content={"success": False,"message": "Internal Server Error"})
