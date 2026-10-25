from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Logical Functions")
print("-"*20)

cursor.execute("""
SELECT
emp_name,
salary,
CASE
WHEN salary>=90000 THEN 'High'
WHEN salary>=75000 THEN 'Medium'
ELSE 'Low'
END
FROM employees
""")

for row in cursor.fetchall():
    print(row)

conn.close()