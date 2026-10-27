import sqlite3
from config import DATABASE_PATH, read_statements

unsafe_template, safe_query = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def one_line(statement):
    lines = [line for line in statement.splitlines() if not line.startswith("--")]
    return " ".join(" ".join(lines).split())


def unsafe_search(name):
    statement = unsafe_template.format(name=name)       # pasting text into SQL: the mistake
    print("  UNSAFE query built:", one_line(statement))
    try:
        cursor.execute(statement)
    except (sqlite3.Warning, sqlite3.ProgrammingError) as error:
        print("  UNSAFE result     : stopped by Python ->", error)
        return
    for row in cursor.fetchall():
        print("  UNSAFE result     :", row)


def safe_search(name):
    cursor.execute(safe_query, (name,))                 # the ? placeholder: the right way
    rows = cursor.fetchall()
    print("  SAFE query        : the ? placeholder, the input is only data")
    for row in rows:
        print("  SAFE result       :", row)
    if not rows:
        print("  SAFE result       : (no rows)")


inputs = [
    ("A normal name", "John"),
    ("An attack: make the test always true", "x' OR '1'='1"),
    ("An attack: sneak in a second command", "x'; DROP TABLE employees; --"),
]

for number, (title, user_input) in enumerate(inputs):
    if number:
        print()
    print(f"{title}: {user_input}")
    print("-" * (len(title) + len(user_input) + 2))
    unsafe_search(user_input)
    safe_search(user_input)

cursor.execute("SELECT COUNT(*) FROM employees")
print("\nEmployees still in the table:", cursor.fetchone()[0])

connection.close()