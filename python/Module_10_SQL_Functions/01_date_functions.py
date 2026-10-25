import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("Current Date")
print("------------")

cursor.execute("SELECT DATE('now')")
print(cursor.fetchone()[0])

print("\nCurrent Time")
print("------------")

cursor.execute("SELECT TIME('now')")
print(cursor.fetchone()[0])

print("\nCurrent DateTime")
print("----------------")

cursor.execute("SELECT DATETIME('now')")
print(cursor.fetchone()[0])

print("\nEmployee Joining Dates")
print("----------------------")

cursor.execute("""
SELECT emp_name,
       joining_date
FROM employees
""")

for row in cursor.fetchall():
    print(row)

connection.close()