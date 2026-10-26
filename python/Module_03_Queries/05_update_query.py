import sqlite3
from config import DATABASE_PATH, read_statements

(read_before, update_one, update_raise, update_multi,
 read_after, update_all, count_inactive) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("Before the updates", read_before)

cursor.execute(update_one)
print("\nOne row, one value    :", cursor.rowcount, "row changed")
cursor.execute(update_raise)
print("A 10% raise (dept 3)  :", cursor.rowcount, "rows changed")
cursor.execute(update_multi)
print("Two columns at once   :", cursor.rowcount, "row changed")
connection.commit()

print()
show("After the updates", read_after)

print("\nDANGER: UPDATE without WHERE")
print("----------------------------")
cursor.execute(update_all)
print("Rows changed            :", cursor.rowcount)
cursor.execute(count_inactive)
print("Inactive before rollback:", cursor.fetchone()[0])

connection.rollback()
cursor.execute(count_inactive)
print("Inactive after rollback :", cursor.fetchone()[0], "<- the change was undone")

connection.close()