from enum import Enum

class Priority(Enum):
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    LOW = "LOW"

class Task:
    def __init__(self, user_id: int, header: str, details: str, priority=Priority.NORMAL, is_executed=False):
        self.user_id = user_id
        self.header = header
        self.details = details
        self.priority = priority
        self.is_executed = is_executed
    
    def complete_task(self):
        self.is_executed = True

    def cancel_task(self):
        self.is_executed = False

    def update_task_details(self, new_header, new_details):
        self.header = new_header
        self.details = new_details

    def change_task_priority(self, new_priority):
        self.priority = new_priority

    def get_task_info(self):
        return f"Header: {self.header}, Details: {self.details}, Priority: {self.priority}, Executed: {self.is_executed}"
