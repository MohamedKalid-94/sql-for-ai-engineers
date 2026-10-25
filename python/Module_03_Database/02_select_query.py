import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

print("Employees")
print("-"*60)

for row in rows:
    print(row)

connection.close()