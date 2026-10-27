import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "NULL does maths and comparisons strangely (None is NULL)",
    "IS NULL: employees with no phone",
    "IS NOT NULL: employees with a phone",
    "COUNT(*) counts rows, COUNT(column) skips NULLs",
    "Sorting: NULLs come first",
    "NULLS LAST: NULLs go to the end",
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