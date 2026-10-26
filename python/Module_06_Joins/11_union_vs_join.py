import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "JOIN: two columns side by side (names matched to departments)",
    "UNION: one column, employee names and department names stacked",
    "Shape comparison: rows from the JOIN and rows from the UNION",
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