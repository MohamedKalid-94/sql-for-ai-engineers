import sqlite3
from config import DATABASE_PATH, read_statements

read_rows, update_from, update_subquery = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("Before the updates", read_rows)

cursor.execute(update_from)
print("\nUPDATE ... FROM, a 10% raise for the AI department:", cursor.rowcount, "rows changed")

cursor.execute(update_subquery)
print("Subquery way, +1000 for the Python department:", cursor.rowcount, "row changed")

print()
show("After the updates (not saved yet)", read_rows)

connection.rollback()

print()
show("After rollback (salaries are back)", read_rows)

connection.close()