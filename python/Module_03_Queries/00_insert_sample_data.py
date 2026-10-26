import sqlite3
from config import DATABASE_PATH, read_statements

count_before, insert_sample, read_all = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(count_before)
print("Employees before:", cursor.fetchone()[0])

cursor.execute(insert_sample)
connection.commit()
print("Rows inserted   :", cursor.rowcount)

print("\nEmployees now")
print("-------------")
cursor.execute(read_all)
for row in cursor.fetchall():
    print(row)

connection.close()