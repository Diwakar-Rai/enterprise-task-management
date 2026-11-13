from fastapi import FastAPI

from app.core.config import settings
from app.core.lifespan import lifespan
from app.api.router import router

from app.exceptions.base import AppException

from app.exceptions.handlers import app_exception_handler, generic_exception_handler

from app.middleware.request_middleware import request_middleware

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG, lifespan=lifespan)

app.middleware("http")(request_middleware)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(router, prefix="/api/v1")
