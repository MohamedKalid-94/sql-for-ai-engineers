import sqlite3
from config import DATABASE_PATH, read_statements

native_full, left_plus_unmatched = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    try:
        cursor.execute(statement)
    except sqlite3.OperationalError as error:
        print("This SQLite is too old for it (needs 3.39 or newer):", error)
        return
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("(no rows)")


show("FULL JOIN: Maria (no department) and Cloud (no employee) both appear", native_full)
print()
show("Same answer on any SQLite: LEFT JOIN + the unmatched rows, joined with UNION ALL", left_plus_unmatched)

connection.close()