import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "CAST: change a value from one type to another",
    "CAST never fails: odd inputs give odd answers",
    "SQLite also converts quietly: + is maths, || joins text",
    "A text number still matches a number column (column affinity)",
    "printf: turn numbers into formatted text",
    "CAST between bytes and text",
    "Salary as text for a report, and as a whole number",
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