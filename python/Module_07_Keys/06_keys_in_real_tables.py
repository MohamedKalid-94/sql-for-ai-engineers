import sqlite3
from config import DATABASE_PATH, read_statements

table_info, index_list, foreign_key_list = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("PRIMARY KEY of employees")
print("------------------------")
cursor.execute(table_info)
print([row[1] for row in cursor.fetchall() if row[5]])

print("\nUNIQUE keys of employees (SQLite builds a hidden index for each one)")
print("--------------------------------------------------------------------")
cursor.execute(index_list)
for row in cursor.fetchall():       # (number, name, unique, made_by, partial)
    print(f"{row[1]} | unique: {row[2]} | made by: {row[3]} (u = a UNIQUE rule)")

print("\nFOREIGN KEYS of employees")
print("-------------------------")
cursor.execute(foreign_key_list)
foreign_keys = sorted(cursor.fetchall(), key=lambda row: row[3])   # (id, seq, table, from, to, ...)
for row in foreign_keys:
    print(f"{row[3]} -> {row[2]}({row[4]})")

connection.close()