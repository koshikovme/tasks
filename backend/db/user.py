import hashlib
from db.database import execute
from db.database import FetchMode

def hash_password(password):
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    return hashed_password

def create_user(username: str, password: str):
    hashed_password = hash_password(password)

    stmt = """
    INSERT INTO users (username, password)
    VALUES (?, ?);
    """
    values = (username, hashed_password)

    print(execute(stmt, values, is_commitable=True))

def user_exists(username, hashed_password):
    stmt = """
    SELECT COUNT(*) FROM users WHERE username = ? AND password = ?;
    """
    values = (username, hashed_password)
    result = execute(stmt, values, is_fetchable=True)
    print("result is : ", result)
    return result

def get_tasks(user_id):
    stmt = """
    SELECT * FROM tasks WHERE user_id = ?;
    """
    values = (user_id,)
    result = execute(stmt, values, is_fetchable=True, fetch_strategy=FetchMode.all)
    print("result is : ", result)
    return result