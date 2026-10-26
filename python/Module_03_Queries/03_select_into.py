import sqlite3
from config import DATABASE_PATH, read_statements

create_table, read_rows, describe_table = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
connection.commit()
print("Table high_earners created from a SELECT")

print("\nRows copied into the new table")
print("------------------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

cursor.execute(describe_table)
print("\nColumns of high_earners:", [row[1] for row in cursor.fetchall()])

connection.close()