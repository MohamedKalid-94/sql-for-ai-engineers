import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "Highest salary first (ties broken by name)",
    "By department, then highest salary",
    "By joining date (NULL dates come first)",
    "Top 3 salaries (ORDER BY + LIMIT)",
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