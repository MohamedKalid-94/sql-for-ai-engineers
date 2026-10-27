import sqlite3
from config import DATABASE_PATH, read_statements

select_staff, raise_salary, taxed_list = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def get_staff(dept, min_salary):
    """Procedure 1: list the staff of a department above a salary."""
    cursor.execute(select_staff, {"dept": dept, "min_salary": min_salary})
    return cursor.fetchall()


def give_raise(dept, percent):
    """Procedure 2: raise every salary in a department by a percent."""
    cursor.execute(raise_salary, {"dept": dept, "percent": percent})
    return cursor.rowcount


def income_tax(salary):
    """A Python function that SQL can call: 10 percent of the salary."""
    return round(salary * 0.10, 2)


print("Calling get_staff(dept, min_salary) with different arguments")
print("------------------------------------------------------------")
for dept, min_salary in [(1, 0), (1, 80000), (2, 0)]:
    print(f"get_staff({dept}, {min_salary}) ->", get_staff(dept, min_salary))

print("\nCalling give_raise(1, 10)")
print("-------------------------")
print("Rows changed:", give_raise(1, 10))
print("get_staff(1, 0) ->", get_staff(1, 0))
connection.rollback()
print("After rollback  ->", get_staff(1, 0))

print("\nA Python function used inside SQL")
print("---------------------------------")
connection.create_function("income_tax", 1, income_tax)
cursor.execute(taxed_list)
for row in cursor.fetchall():
    print(row)

connection.close()