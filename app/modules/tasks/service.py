class TaskService:
    def __init__(self, repository):
        self.repository = repository 

    def create_task(self, task_data):
        return self.repository.create(task_data)

    def get_tasks(self):
        return self.repository.get_all()