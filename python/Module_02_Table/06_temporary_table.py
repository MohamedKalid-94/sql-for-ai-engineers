import sqlite3
from config import DATABASE_PATH, read_statements

create_temp, read_temp, list_temp_tables = read_statements(__file__)

# Connection 1: the temporary table lives here
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()
cursor.execute(create_temp)

print("Inside the first connection")
print("---------------------------")
cursor.execute(read_temp)
for row in cursor.fetchall():
    print(row)

cursor.execute(list_temp_tables)
print("Temporary tables:", [name for (name,) in cursor.fetchall()])
connection.close()

# Connection 2: a new connection to the same file cannot see it
connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("\nInside a second connection")
print("--------------------------")
cursor.execute(list_temp_tables)
print("Temporary tables:", [name for (name,) in cursor.fetchall()])

try:
    cursor.execute(read_temp)
except sqlite3.OperationalError as error:
    print("Rejected:", error)

connection.close()