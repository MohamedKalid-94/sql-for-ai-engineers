import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "COALESCE: fill a missing phone",
    "IFNULL: fill a missing joining date",
    "COALESCE with many values: phone first, then email",
    "NULLIF: NULL when the two values are equal",
    "NULLIF hides 65000 from AVG, as if it were unknown",
    "IIF: a short if / else",
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