import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "ANY equivalent: above the smallest salary of departments 3 and 5",
    "ALL equivalent: above the largest salary of departments 3 and 5",
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