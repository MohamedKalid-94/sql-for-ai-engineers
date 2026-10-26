import sqlite3
from config import DATABASE_PATH, read_statements

(create_high_salary, create_details, list_views,
 read_high_salary, read_details, raise_david) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_high_salary)
cursor.execute(create_details)
connection.commit()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("Views in this database", list_views)

print()
show("high_salary_employees (salary >= 80000)", read_high_salary)

print()
show("employee_details (employees joined with department names)", read_details)

print("\nA view is live: change the TABLE and the VIEW changes")
cursor.execute(raise_david)

print()
show("high_salary_employees after David's raise (not saved yet)", read_high_salary)

connection.rollback()

print()
show("high_salary_employees after rollback", read_high_salary)

connection.close()