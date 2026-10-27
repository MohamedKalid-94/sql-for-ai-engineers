import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, insert_valid, insert_duplicate,
 insert_null_one, insert_null_two, read_rows) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_valid)
connection.commit()
print("Two accounts created")

print("\nTry to reuse an email that is already taken")
try:
    cursor.execute(insert_duplicate)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

print("\nTwo accounts with no email at all (NULL is allowed many times)")
cursor.execute(insert_null_one)
cursor.execute(insert_null_two)
connection.commit()
print("Both accepted")

print("\nAccounts in the table")
print("---------------------")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

connection.close()