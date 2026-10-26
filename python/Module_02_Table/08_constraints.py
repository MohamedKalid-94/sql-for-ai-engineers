import sqlite3
from config import get_connection, read_statements

(create_table, insert_valid, read_rows, bad_primary_key,
 bad_unique, bad_not_null, bad_check, bad_foreign_key) = read_statements(__file__)

# get_connection() switches foreign keys ON. SQLite leaves them OFF unless we ask.
connection = get_connection()
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_valid)
connection.commit()

print("The valid row (status was filled in by DEFAULT)")
print("-----------------------------------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

print("\nRows that break a rule")
print("----------------------")
rejected = [
    ("PRIMARY KEY", bad_primary_key),
    ("UNIQUE", bad_unique),
    ("NOT NULL", bad_not_null),
    ("CHECK", bad_check),
    ("FOREIGN KEY", bad_foreign_key),
]
for rule, statement in rejected:
    try:
        cursor.execute(statement)
        print(f"{rule:<12}: unexpectedly accepted")
    except sqlite3.IntegrityError as error:
        print(f"{rule:<12}: rejected -> {error}")

print("\nRows in the table after all attempts")
print("------------------------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

connection.close()