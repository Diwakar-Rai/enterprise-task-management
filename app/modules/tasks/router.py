from fastapi import APIRouter, Depends, status, Query
from app.modules.tasks.schemas import TaskCreate, TaskResponse, TaskListResponse
from app.modules.tasks.service import TaskService
from app.dependencies.task_dependencies import get_task_service

router = APIRouter()


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    task_data: TaskCreate, service: TaskService = Depends(get_task_service)
):
    return service.create_task(task_data)


@router.get("/", response_model=TaskListResponse)
def get_tasks(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    search: str | None = Query(default=None, min_length=1),
    sort_by: str = Query(default="id", pattern="^(id|title)$"),
    sort_order: str = Query(default="asc", pattern="^(asc|desc)$"),
    service: TaskService = Depends(get_task_service),
):
    return service.get_tasks(
        page=page,
        page_size=page_size,
        search=search,
        sort_by=sort_by,
        sort_order=sort_order,
    )


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.get_task_by_id(task_id)
