from fastapi import Depends
from app.modules.tasks.repository import TaskRepository
from app.modules.tasks.service import TaskService

task_repository = TaskRepository()


def get_task_repository() -> TaskRepository:
    return task_repository


def get_task_service(
    repository: TaskRepository = Depends(get_task_repository),
) -> TaskService:
    return TaskService(repository)
