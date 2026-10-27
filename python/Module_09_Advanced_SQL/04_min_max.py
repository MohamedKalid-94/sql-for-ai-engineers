import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "Lowest and highest salary",
    "Who earns the highest salary",
    "Lowest and highest salary in each department",
    "MIN and MAX on text and dates (NULL dates are ignored)",
    "MAX of nothing: the Cloud department has no employees",
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