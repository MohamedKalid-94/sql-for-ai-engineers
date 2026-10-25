import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("COUNT")
print("-----")

cursor.execute("""
SELECT COUNT(*)
FROM employees
""")

print(cursor.fetchone()[0])

print("\nSUM")
print("---")

cursor.execute("""
SELECT SUM(salary)
FROM employees
""")

print(cursor.fetchone()[0])

print("\nAVG")
print("---")

cursor.execute("""
SELECT AVG(salary)
FROM employees
""")

print(cursor.fetchone()[0])

print("\nMIN")
print("---")

cursor.execute("""
SELECT MIN(salary)
FROM employees
""")

print(cursor.fetchone()[0])

print("\nMAX")
print("---")

cursor.execute("""
SELECT MAX(salary)
FROM employees
""")

print(cursor.fetchone()[0])

connection.close()