import sqlite3
from config import DATABASE_PATH, read_statements

read_rows, raise_department, insert_department, delete_department = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("1. What a cursor knows after a SELECT")
print("-------------------------------------")
cursor.execute(read_rows)
print("Column names (description):", [column[0] for column in cursor.description])
print("Rows counted (rowcount)   :", cursor.rowcount, "<- -1 means a SELECT does not count rows")
print("Batch size (arraysize)    :", cursor.arraysize)

print("\n2. Fetching in batches of 2 (fetchmany)")
print("---------------------------------------")
cursor.arraysize = 2
batch_number = 0
while True:
    batch = cursor.fetchmany()
    if not batch:
        break
    batch_number += 1
    print(f"Batch {batch_number}:", batch)

print("\n3. Reading a row by column name (row_factory)")
print("---------------------------------------------")
connection.row_factory = sqlite3.Row
named_cursor = connection.cursor()
named_cursor.execute(read_rows)
first = named_cursor.fetchone()
print("first['name']  :", first["name"])
print("first['salary']:", first["salary"])
print("as a dict      :", dict(first))
print("keys           :", first.keys())
named_cursor.close()
connection.row_factory = None

print("\n4. What a cursor reports after changing data")
print("--------------------------------------------")
cursor.execute(raise_department, (1,))
print("UPDATE rowcount          :", cursor.rowcount, "rows changed")
cursor.execute(insert_department, ("Robotics",))
print("INSERT lastrowid         :", cursor.lastrowid, "<- the id the new row received")
print("INSERT rowcount          :", cursor.rowcount)
cursor.execute(delete_department, ("Robotics",))
print("DELETE rowcount          :", cursor.rowcount)
print("connection.total_changes :", connection.total_changes)

connection.rollback()
cursor.execute(read_rows)
print("\nAfter rollback, John's salary is back to:", cursor.fetchone()[2])

connection.close()