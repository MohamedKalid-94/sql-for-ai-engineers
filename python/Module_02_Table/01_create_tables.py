import sqlite3
from config import DATABASE_PATH, read_statements

(create_departments, create_employees, insert_departments, insert_employees,
 read_departments, read_employees) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_departments)
cursor.execute(create_employees)
cursor.execute(insert_departments)
cursor.execute(insert_employees)
connection.commit()
print("Tables created and filled")

print("\ndepartments")
print("-----------")
cursor.execute(read_departments)
for row in cursor.fetchall():
    print(row)

print("\nemployees")
print("---------")
cursor.execute(read_employees)
for row in cursor.fetchall():
    print(row)

connection.close()