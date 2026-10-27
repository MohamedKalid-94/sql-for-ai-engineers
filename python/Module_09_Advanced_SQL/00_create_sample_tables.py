import sqlite3
from config import DATABASE_PATH, read_statements

remove_dates, read_rows = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(remove_dates)
connection.commit()
print("Joining date removed for", cursor.rowcount, "employees")

print("\nemployees (None means the value is missing)")
print("-------------------------------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

connection.close()