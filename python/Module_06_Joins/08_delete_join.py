import sqlite3
from config import DATABASE_PATH, read_statements

read_with_departments, delete_by_department, delete_orphans, read_after = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("Before the deletes", read_with_departments)

cursor.execute(delete_by_department)
print("\nDelete 1, employees of the GenAI department:", cursor.rowcount, "row removed")

cursor.execute(delete_orphans)
print("Delete 2, employees with no matching department:", cursor.rowcount, "row removed")

print()
show("After the deletes (not saved yet)", read_after)

connection.rollback()

print()
show("After rollback (everyone is back)", read_with_departments)

connection.close()