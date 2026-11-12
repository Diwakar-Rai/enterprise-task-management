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

    def get_all(self):
        return self.tasks
