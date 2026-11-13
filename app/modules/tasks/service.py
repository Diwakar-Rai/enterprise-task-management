import math

from app.modules.tasks.exceptions import TaskNotFoundException

class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, task_data):
        return self.repository.create(task_data)

    def get_tasks(
        self,
        page: int,
        page_size: int,
        search: str | None,
        sort_by: str,
        sort_order: str,
    ):
        offset = (page - 1) * page_size
        result = self.repository.get_all(
            offset=offset,
            limit=page_size,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )

        total_pages = math.ceil(result["total"]/page_size)

        return {
            "items": result["items"],
            "total": result["total"],
            "page": page, 
            "page_size": page_size,
            "total_pages": total_pages
        }

    def get_task_by_id(self, task_id: int):
        task = self.repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundException(task_id)
        return task
