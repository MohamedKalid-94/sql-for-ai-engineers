import sqlite3
from config import DATABASE_PATH, read_statements

(list_views, create_directory, drop_details,
 read_directory, alter_view) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("Views before the rename", list_views)

cursor.execute(create_directory)
cursor.execute(drop_details)
connection.commit()

print()
show("Views after the rename (employee_details -> employee_directory)", list_views)

print()
show("The data, read through the new name", read_directory)

print("\nALTER VIEW ... RENAME (works in other databases, not in SQLite)")
try:
    cursor.execute(alter_view)
except sqlite3.Error as error:
    print("Rejected:", error)

connection.close()