import sqlite3
from pathlib import Path
from config import DATABASE_PATH, read_statements

show_list, attach_scratch, show_list_again = read_statements(__file__)


def print_databases(cursor, statement):
    cursor.execute(statement)
    for number, name, file in cursor.fetchall():
        file_name = Path(file).name if file else "(memory)"
        print(f"{number} | {name:<8} | {file_name}")


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("Notebooks in the bag now")
print("------------------------")
print_databases(cursor, show_list)

cursor.execute(attach_scratch)

print("\nAfter attaching a scratch notebook")
print("----------------------------------")
print_databases(cursor, show_list_again)

connection.close()