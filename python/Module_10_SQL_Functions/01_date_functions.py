import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "Year and month of each joining date",
    "How long each person has worked, as of 2025-06-01",
    "The weekday each person joined",
    "Calendar helpers, all worked out from 2025-03-15",
    "Unix timestamps: seconds since 1 January 1970",
    "How many people joined in each year",
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