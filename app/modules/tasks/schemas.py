from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None = None

class TaskListResponse(BaseModel):
    items: list[TaskResponse]
    total: int 
    page: int 
    page_size: int 
    total_pages: int 

    