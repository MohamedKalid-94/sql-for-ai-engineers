import sqlite3
from config import DATABASE_PATH, read_statements

insert_maria, read_employees, read_departments = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(insert_maria)
connection.commit()
print("Maria added (she has no department)")

print("\nemployees (dept_id None means no department)")
print("--------------------------------------------")
cursor.execute(read_employees)
for row in cursor.fetchall():
    print(row)

print("\ndepartments (Cloud has no employees)")
print("------------------------------------")
cursor.execute(read_departments)
for row in cursor.fetchall():
    print(row)

connection.close()