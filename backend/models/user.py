from task import Task

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.task_list = []
    
    def add_task(self, task):
        self.task_list.append(task)
    
    def remove_task(self, task):
        self.task_list.remove(task)
    
    def get_tasks(self):
        return self.task_list