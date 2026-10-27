import sqlite3
from config import DATABASE_PATH, read_statements

(plan_before, create_salary_index, plan_after, plan_calculation,
 create_dept_index, plan_covering) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show_plan(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print("  ", row[3])      # the fourth column holds the plan text


show_plan("No index on salary: every row is read", plan_before)

cursor.execute(create_salary_index)
connection.commit()
print("\nIndex created: idx_employees_salary")

show_plan("The same query with the index", plan_after)
show_plan("Tip 2: salary + 0 hides the column, so the index is NOT used", plan_calculation)

cursor.execute(create_dept_index)
connection.commit()
print("\nIndex created: idx_employees_dept_salary (dept_id, salary)")

show_plan("Tip 3: the index holds both columns the query needs (COVERING)", plan_covering)

connection.close()