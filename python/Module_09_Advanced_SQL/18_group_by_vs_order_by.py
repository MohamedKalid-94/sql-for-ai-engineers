import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "ORDER BY: every employee, just sorted (5 rows)",
    "GROUP BY: one row for each department (4 rows)",
    "GROUP BY, then ORDER BY the totals",
    "How many rows each one gives back",
    "GROUP BY with LEFT JOIN: even Cloud shows up, with 0 staff",
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