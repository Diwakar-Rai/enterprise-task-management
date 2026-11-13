class TaskRepository:
    def __init__(self):
        self.tasks = []
        self.current_id = 1

    def create(self, task_data):
        task = {
            "id": self.current_id,
            "title": task_data.title,
            "description": task_data.description,
        }

        self.tasks.append(task)
        self.current_id += 1
        return task

    def get_all(
        self, offset: int, limit: int, search: str | None, sort_by: str, sort_order: str
    ):
        tasks = self.tasks.copy()

        if search:
            tasks = [task for task in tasks if search.lower() in task["title"].lower()]

        tasks = sorted(
            tasks, key=lambda task: task[sort_by], reverse=(sort_order == "desc")
        )

        total=len(tasks)
        paginated_tasks = tasks[offset: offset + limit] 

        return {"items": paginated_tasks, "total": total}

    def get_by_id(self, task_id: int):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
