import sqlite3
from config import DATABASE_PATH, read_statements

create_table, insert_row, read_rows = read_statements(__file__)

print("Before: database file exists =", DATABASE_PATH.exists())

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_row)
connection.commit()

print("After : database file exists =", DATABASE_PATH.exists())

print("\nRows in database_info")
print("---------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

connection.close()