import sqlite3
from config import DATABASE_PATH, read_statements

(david_no_date, alex_inactive, create_contractors, insert_contractors,
 read_employees, read_contractors) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(david_no_date)
cursor.execute(alex_inactive)
cursor.execute(create_contractors)
cursor.execute(insert_contractors)
connection.commit()
print("Module 5 extra data created")

print("\nemployees (David has no joining date, Alex is inactive)")
print("-------------------------------------------------------")
cursor.execute(read_employees)
for row in cursor.fetchall():
    print(row)

print("\ncontractors (Sara is in both groups on purpose)")
print("-----------------------------------------------")
cursor.execute(read_contractors)
for row in cursor.fetchall():
    print(row)

connection.close()