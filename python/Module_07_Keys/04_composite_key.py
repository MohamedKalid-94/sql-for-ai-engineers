import sqlite3
from config import DATABASE_PATH, read_statements

create_table, insert_valid, read_rows, insert_duplicate_pair = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_valid)
connection.commit()
print("Three enrollments added")
print("Student 1 is in two classes, and class 1 has two students: all allowed")

print("\nEnrollments in the table")
print("------------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

print("\nTry to enroll student 1 in class 1 a second time")
try:
    cursor.execute(insert_duplicate_pair)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

connection.close()