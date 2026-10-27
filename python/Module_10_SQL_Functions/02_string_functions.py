import sqlite3
from config import DATABASE_PATH, read_statements

titles = [
    "UPPER, LOWER and LENGTH",
    "SUBSTR and INSTR: split an email at the @",
    "Joining text with || and formatting with printf",
    "TRIM, LTRIM and RTRIM remove unwanted characters",
    "Clean messy names: first letter big, the rest small",
    "REPLACE, UNICODE, CHAR, HEX and INSTR",
    "Count the words in a sentence (count the spaces, add 1)",
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