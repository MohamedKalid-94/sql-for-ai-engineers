import sqlite3
from config import DATABASE_PATH, read_statements

create_table, insert_valid, insert_bad, read_rows = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_valid)
connection.commit()
print("Table trainees created and a valid row inserted")

print("\nInsert a row with no name (breaks NOT NULL)")
try:
    cursor.execute(insert_bad)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

print("\nRows in the table (only the valid one got in)")
print("---------------------------------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

connection.close()