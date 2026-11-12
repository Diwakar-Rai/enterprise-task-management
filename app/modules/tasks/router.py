from fastapi import APIRouter, Depends, status
from app.modules.tasks.schemas import TaskCreate, TaskResponse
from app.modules.tasks.service import TaskService
from app.dependencies.task_dependencies import get_task_service

router = APIRouter()


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    task_data: TaskCreate, service: TaskService = Depends(get_task_service)
):
    return service.create_task(task_data)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()
