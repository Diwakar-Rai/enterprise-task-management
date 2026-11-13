import time
import logging

from fastapi import Request

logger = logging.getLogger(__name__)


async def request_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    logger.info("Incoming request: %s %s", request.method, request.url.path)

    response = await call_next(request)

    execution_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(execution_time)

    logger.info(
        "Completed request: %s %s | Status: %s | Time: %.4fs",
        request.method,
        request.url.path,
        response.status_code,
        execution_time,
    )
    return response
