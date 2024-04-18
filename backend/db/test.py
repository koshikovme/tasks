from database import execute


def add_is_done_field():
    stmt = """
    ALTER TABLE tasks ADD COLUMN is_done INTEGER DEFAULT 0;

    """
    execute(stmt, is_commitable=True)

add_is_done_field()

