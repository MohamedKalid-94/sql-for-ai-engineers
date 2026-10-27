import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, insert_defaults, insert_override,
 bad_null, read_rows, show_defaults) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_defaults)
print("Two tickets added with only a title:", cursor.rowcount, "rows")
cursor.execute(insert_override)
print("One ticket added with its own status and priority:", cursor.rowcount, "row")
connection.commit()

print("\nTry to write NULL into status on purpose")
try:
    cursor.execute(bad_null)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

print("\nTickets (the first two got their values from DEFAULT)")
print("-----------------------------------------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

print("\nThe defaults SQLite remembers")
print("-----------------------------")
cursor.execute(show_defaults)
for column_name, default_value in cursor.fetchall():
    print(f"{column_name:<9}: {default_value}")

connection.close()