import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "ROUND and ABS",
    "Division with whole numbers versus decimals",
    "MAX and MIN with several arguments (a floor and a cap)",
    "A raise and a monthly pay, rounded to 2 decimals",
]
*statements, math_statement = read_statements(__file__)
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

print("\nMath functions: CEIL, FLOOR, SQRT and POWER")
print("-------------------------------------------")
try:
    cursor.execute(math_statement)
    print(cursor.fetchone())
except sqlite3.OperationalError as error:
    print("This SQLite build has no math functions:", error)

connection.close()