import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "One value: employees earning above the company average",
    "A list: employees in the AI or GenAI departments",
    "In the column list: how far each salary is from the average",
    "A small table: departments whose average salary is above 75000",
    "Correlated: employees earning above their own department average",
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