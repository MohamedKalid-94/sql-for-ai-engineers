import sqlite3
from config import DATABASE_PATH, read_statements

count_rows, delete_one, preview, delete_condition, delete_all = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def count():
    cursor.execute(count_rows)
    return cursor.fetchone()[0]


print("Rows at the start       :", count())

cursor.execute(delete_one)
print("DELETE by id            :", cursor.rowcount, "row removed")

print("\nPreview of the next delete (SELECT with the same WHERE)")
print("-------------------------------------------------------")
cursor.execute(preview)
for row in cursor.fetchall():
    print(row)

cursor.execute(delete_condition)
print("\nDELETE with a condition :", cursor.rowcount, "row(s) removed")
connection.commit()
print("Rows after commit       :", count())

cursor.execute(delete_all)
print("\nDELETE without WHERE    :", cursor.rowcount, "row(s) removed (not saved yet)")
print("Rows before rollback    :", count())

connection.rollback()
print("Rows after rollback     :", count(), "<- the rows came back")

connection.close()