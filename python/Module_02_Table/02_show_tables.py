import sqlite3
from config import DATABASE_PATH, read_statements

list_tables, describe_employees = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("Tables in this database (SHOW TABLES)")
print("-------------------------------------")
cursor.execute(list_tables)
for (name,) in cursor.fetchall():
    print(name)

print("\nColumns of employees (DESCRIBE)")
print("-------------------------------")
cursor.execute(describe_employees)
for number, name, data_type, not_null, default, primary_key in cursor.fetchall():
    print(f"{number} | {name:<8} | {data_type:<8} | not null: {not_null} | primary key: {primary_key}")

connection.close()