import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "Names starting with S",
    "Names ending with a",
    "Names with exactly 4 letters (each _ is one letter)",
    "Names containing ri",
    "Lower case s still matches (LIKE ignores case)",
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