import sqlite3
from config import DATABASE_PATH, read_statements

(create_students, insert_two, insert_automatic, insert_duplicate,
 read_students, create_codes, insert_null_code, read_codes) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_students)
cursor.execute(insert_two)
cursor.execute(insert_automatic)
connection.commit()
print("Three students added (Meena got her id automatically)")

print("\nTry to give a new student the id 1")
try:
    cursor.execute(insert_duplicate)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

print("\nStudents in the table")
print("---------------------")
cursor.execute(read_students)
for row in cursor.fetchall():
    print(row)

print("\nA surprise: a TEXT primary key without NOT NULL")
print("-----------------------------------------------")
cursor.execute(create_codes)
cursor.execute(insert_null_code)
connection.commit()
cursor.execute(read_codes)
for row in cursor.fetchall():
    print(row)
print("SQLite accepted a NULL primary key. Add NOT NULL to a TEXT key to be safe.")

connection.close()