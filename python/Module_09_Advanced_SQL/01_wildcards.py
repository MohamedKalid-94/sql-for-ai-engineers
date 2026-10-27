import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "Names starting with S (%)",
    "Emails whose name part ends in a",
    "Second letter is a (_a%)",
    "GLOB range: names starting with A to D",
    "LIKE is not case sensitive: s% finds Sara",
    "GLOB is case sensitive: s% finds nobody",
    "A % in the pattern matches anything, so both rows come back",
    "ESCAPE makes the % a real % sign, so only one row matches",
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