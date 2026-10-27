import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "A simple CTE: the high earners",
    "A CTE joined to the tables: each salary beside its department average",
    "A recursive CTE that counts from 1 to 5",
    "A recursive CTE that walks the company tree (level, name, path)",
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