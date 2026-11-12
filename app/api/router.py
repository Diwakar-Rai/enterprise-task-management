from fastapi import APIRouter
from app.modules.tasks.router import router as task_router

router = APIRouter()

router.include_router(task_router, prefix="/tasks", tags=["Tasks"])


@router.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Enterprise Task Management API is running"}
