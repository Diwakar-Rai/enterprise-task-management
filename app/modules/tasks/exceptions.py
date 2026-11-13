from app.exceptions.base import AppException 

class TaskNotFoundException(AppException):
    def __init__(self, task_id: int):
        super().__init__(message=f"Task with ID {task_id} not found", status_code=404)