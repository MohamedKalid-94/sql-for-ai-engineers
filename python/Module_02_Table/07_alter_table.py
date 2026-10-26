import sqlite3
from config import DATABASE_PATH, read_statements

(add_phone, add_is_active, read_rows, rename_column,
 drop_column, show_columns, unsupported) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def print_columns(title):
    cursor.execute(show_columns)
    print(f"{title:<22}:", [row[1] for row in cursor.fetchall()])


print_columns("Columns at the start")

cursor.execute(add_phone)
cursor.execute(add_is_active)
connection.commit()
print_columns("After ADD COLUMN")

print("\nExisting rows get NULL for phone and the DEFAULT for is_active")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print("  ", row)

cursor.execute(rename_column)
connection.commit()
print()
print_columns("After RENAME COLUMN")

cursor.execute(drop_column)
connection.commit()
print_columns("After DROP COLUMN")

print("\nChanging a column type")
try:
    cursor.execute(unsupported)
except sqlite3.OperationalError as error:
    print("Rejected:", error)

connection.close()