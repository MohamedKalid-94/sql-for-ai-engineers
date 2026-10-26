import sqlite3
from config import DATABASE_PATH, read_statements

native_right, swapped_left, no_employees = read_statements(__file__)

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


show("RIGHT JOIN: every department (Cloud has no employee)", native_right)
print()
show("Same answer on any SQLite: swap the tables and use LEFT JOIN", swapped_left)
print()
show("Departments with no employees", no_employees)

connection.close()