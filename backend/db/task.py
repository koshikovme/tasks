from db.database import execute, FetchMode

def sorted_tasks(user_id, sort_by='id'):
    stmt = f"SELECT * FROM tasks WHERE user_id = ? ORDER BY {sort_by}"
    return execute(stmt, (user_id,), is_fetchable=True, fetch_strategy=FetchMode.all)

def add_task(header: str, details: str, priority: str, user_id:int):
    stmt = """
    INSERT INTO tasks (header, details, priority, user_id, is_done) VALUES (?, ?, ?, ?, ?);
    """
    values = (header, details, priority, user_id, 0)

    print(execute(stmt, values, is_commitable=True))

def remove_task(task_id: int):
    stmt = """
    DELETE FROM tasks WHERE id = ?;
    """
    values = (task_id,)

    print(execute(stmt, values, is_commitable=True))

def update_priority(task_id: int, new_priority: str):
    stmt = """
    UPDATE tasks 
    SET priority = ? 
    WHERE id = ?;
    """
    values = (new_priority, task_id)

    print(execute(stmt, values, is_commitable=True))

    
def update_status(task_id: int, is_done: int):
    stmt = """
    UPDATE tasks 
    SET is_done = ? 
    WHERE id = ?;
    """
    values = (is_done, task_id)

    print(execute(stmt, values, is_commitable=True))


