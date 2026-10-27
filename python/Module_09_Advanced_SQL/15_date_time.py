import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "date, time and datetime clean a value",
    "Calendar maths (note: Jan 31 plus 1 month lands in March)",
    "Days between the joining date and 2025-06-01",
    "strftime formats a date any way we like",
    "Weekday numbers (0 is Sunday, 6 is Saturday)",
    "date('now') changes every day, so only its shape is checked",
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