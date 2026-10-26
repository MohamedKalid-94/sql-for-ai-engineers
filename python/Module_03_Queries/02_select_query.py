import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "All columns (SELECT *), first 3 rows",
    "Chosen columns, only department 1",
    "A calculated column (salary x 12)",
    "Counting and summarising",
]
statements = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

for number, (title, statement) in enumerate(zip(titles, statements)):
    if number:
        print()
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)

connection.close()