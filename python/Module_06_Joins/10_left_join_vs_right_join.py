import sqlite3
from config import DATABASE_PATH, read_statements

left_join, native_right, swapped_left, gaps = read_statements(__file__)

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


show("LEFT JOIN: every employee is kept", left_join)
print()
show("RIGHT JOIN: every department is kept", native_right)
print()
show("The RIGHT JOIN answer again, with LEFT JOIN and the tables swapped", swapped_left)
print()
show("What each side leaves unmatched", gaps)

connection.close()