import logging 
from contextlib import asynccontextmanager

from fastapi import FastAPI 

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Enterprise Task Management API")
    logger.info("Application resources Initialized")

    yield 

    logger.info("Releasing application resources")
    logger.info("Enterprise Task Management API stopped")