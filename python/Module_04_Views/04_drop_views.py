import sqlite3
from config import DATABASE_PATH, read_statements

(list_views, drop_view, drop_if_exists,
 drop_missing, count_employees) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("Views before DROP", list_views)

cursor.execute(drop_view)
connection.commit()

print()
show("Views after DROP VIEW employee_directory", list_views)

cursor.execute(drop_if_exists)
print("\nDROP VIEW IF EXISTS on a missing view: no error")

try:
    cursor.execute(drop_missing)
except sqlite3.Error as error:
    print("DROP VIEW on a missing view: rejected ->", error)

cursor.execute(count_employees)
print("\nEmployees still in the table:", cursor.fetchone()[0], "<- dropping a view never touches the data")

connection.close()