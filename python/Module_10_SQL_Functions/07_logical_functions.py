import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "CASE: a grade for each of Asha's scores",
    "How many scores earned each grade",
    "IIF: subjects passed and failed (pass mark 60)",
    "AND, OR and NOT give 1 or 0, and NULL when the answer is unknown",
    "CASE with IN: group departments into teams",
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