import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, insert_valid, by_primary_key, by_username, by_email,
 bad_username, bad_email) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_valid)
connection.commit()
print("Two members added")


def show(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("Find a row by its PRIMARY key (member_id = 2)", by_primary_key)
show("Find the same kind of row by an ALTERNATE key (username)", by_username)
show("Find a row by another ALTERNATE key (email)", by_email)

print("\nTry to add a second member called kalid")
try:
    cursor.execute(bad_username)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

print("\nTry to add a member with john's email")
try:
    cursor.execute(bad_email)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

connection.close()