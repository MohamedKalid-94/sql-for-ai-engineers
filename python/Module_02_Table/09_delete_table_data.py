import sqlite3
from config import DATABASE_PATH, read_statements

count_rows, delete_one_department, delete_all = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def count():
    cursor.execute(count_rows)
    return cursor.fetchone()[0]


print("Rows at the start        :", count())

cursor.execute(delete_one_department)
print("DELETE with WHERE        :", cursor.rowcount, "row(s) removed")
connection.commit()
print("Rows after commit        :", count())

cursor.execute(delete_all)
print("\nDELETE without WHERE     :", cursor.rowcount, "row(s) removed (not saved yet)")
print("Rows before rollback     :", count())

connection.rollback()
print("Rows after rollback      :", count(), "<- the rows came back")

cursor.execute(delete_all)
connection.commit()
print("\nRows after delete+commit :", count())

connection.close()