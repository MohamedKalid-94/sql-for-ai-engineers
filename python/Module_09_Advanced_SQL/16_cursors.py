import sqlite3
from config import DATABASE_PATH, read_statements

read_all, update_one, update_all = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("Walking through the rows with a cursor")
print("--------------------------------------")
cursor.execute(read_all)
print("fetchone    :", cursor.fetchone())
print("fetchone    :", cursor.fetchone())
print("fetchmany(2):", cursor.fetchmany(2))
print("fetchall    :", cursor.fetchall(), "<- whatever is left")

print("\nA for loop does the same, one row at a time")
print("-------------------------------------------")
cursor.execute(read_all)
for row in cursor:
    print(row)


def salaries():
    cursor.execute(read_all)
    return [row[2] for row in cursor.fetchall()]


print("\nRow by row: a 5 percent raise, one UPDATE for each employee")
print("-----------------------------------------------------------")
cursor.execute(read_all)
for emp_id, name, salary in cursor.fetchall():
    cursor.execute(update_one, {"new_salary": round(salary * 1.05, 2), "emp_id": emp_id})
row_by_row = salaries()
print("Salaries:", row_by_row)
connection.rollback()

print("\nSet based: the same raise in ONE command")
print("----------------------------------------")
cursor.execute(update_all)
set_based = salaries()
print("Salaries:", set_based)
connection.rollback()

print("\nSame result:", row_by_row == set_based)
print("One command is shorter, and it is faster on big tables.")

connection.close()