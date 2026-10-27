import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "IN: departments that have employees",
    "EXISTS: the same answer",
    "NOT IN: departments with no employees",
    "NOT EXISTS: the same answer",
    "NOT IN trap: John has no manager (NULL), so this finds nobody",
    "NOT EXISTS: employees who manage nobody, found correctly",
]
statements = read_statements(__file__)
assert len(titles) == len(statements), "each title needs exactly one statement"

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

for number, (title, statement) in enumerate(zip(titles, statements)):
    if number:
        print()
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("(no rows)")

connection.close()