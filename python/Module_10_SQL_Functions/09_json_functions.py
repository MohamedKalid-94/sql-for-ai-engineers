from config import get_connection

conn = get_connection()
cursor = conn.cursor()

print("JSON Functions")
print("-"*15)

cursor.execute("""
SELECT
json_object(
'emp_id',emp_id,
'name',emp_name,
'salary',salary
)
FROM employees
LIMIT 3
""")

for row in cursor.fetchall():
    print(row[0])

conn.close()