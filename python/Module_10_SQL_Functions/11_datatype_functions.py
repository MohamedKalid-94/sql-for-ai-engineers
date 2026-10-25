from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Datatype Functions")
print("-"*20)

cursor.execute("""
SELECT
typeof(emp_id),
typeof(emp_name),
typeof(salary),
typeof(joining_date)
FROM employees
LIMIT 1
""")

print(cursor.fetchone())

conn.close()