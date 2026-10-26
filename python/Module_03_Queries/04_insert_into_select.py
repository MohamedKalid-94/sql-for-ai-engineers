import sqlite3
from config import DATABASE_PATH, read_statements

create_backup, insert_select, read_backup, bad_insert = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_backup)
cursor.execute(insert_select)
connection.commit()
print("Rows copied with named columns:", cursor.rowcount)

print("\nRows now in employees_backup")
print("----------------------------")
cursor.execute(read_backup)
for row in cursor.fetchall():
    print(row)

print("\nThe mistake: SELECT * into a table with fewer columns")
try:
    cursor.execute(bad_insert)
except sqlite3.Error as error:
    print("Rejected:", error)

connection.close()