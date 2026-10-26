import sqlite3
from config import DATABASE_PATH, read_statements

(read_view, update_through_view, drop_view, create_view,
 read_new_view, create_or_replace, show_definition) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("high_salary_employees now (salary >= 80000)", read_view)

print("\nMeaning 1: change the DATA through the view")
try:
    cursor.execute(update_through_view)
except sqlite3.Error as error:
    print("Rejected:", error)

print("\nMeaning 2: change the DEFINITION (DROP VIEW, then CREATE VIEW)")
cursor.execute(drop_view)
cursor.execute(create_view)
connection.commit()

show("high_salary_employees after the new definition (salary >= 75000, email added)", read_new_view)

print("\nCREATE OR REPLACE VIEW (works in MySQL, not in SQLite)")
try:
    cursor.execute(create_or_replace)
except sqlite3.Error as error:
    print("Rejected:", error)

print("\nWhat SQLite stored: the question, not the answers")
cursor.execute(show_definition)
print(cursor.fetchone()[0])

connection.close()