import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("UPPER Function")
print("--------------")

cursor.execute("""
SELECT UPPER(emp_name)
FROM employees
""")

for row in cursor.fetchall():
    print(row)

print("\nLOWER Function")
print("--------------")

cursor.execute("""
SELECT LOWER(emp_name)
FROM employees
""")

for row in cursor.fetchall():
    print(row)

print("\nLENGTH Function")
print("---------------")

cursor.execute("""
SELECT emp_name,
       LENGTH(emp_name)
FROM employees
""")

for row in cursor.fetchall():
    print(row)

print("\nSUBSTR Function")
print("---------------")

cursor.execute("""
SELECT emp_name,
       SUBSTR(emp_name,1,3)
FROM employees
""")

for row in cursor.fetchall():
    print(row)

connection.close()