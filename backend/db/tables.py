from database import execute


stmt = """
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255),
    password VARCHAR(255)
);
"""


print(execute(stmt, (), is_commitable=True))


stmt = """
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    header VARCHAR(255),
    details VARCHAR(3000),
    priority TEXT CHECK(priority IN ('NORMAL', 'HIGH', 'LOW')),
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
"""

print(execute(stmt, (), is_commitable=True))


