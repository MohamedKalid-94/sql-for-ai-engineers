import sqlite3
from config import DATABASE_PATH, get_connection, read_statements

(create_classes, create_students, create_homework,
 insert_classes, insert_students, insert_homework,
 check_setting, read_students, read_homework,
 bad_insert, bad_delete, delete_spare_class) = read_statements(__file__)

# get_connection() switches foreign key checking ON
connection = get_connection()
cursor = connection.cursor()

cursor.execute(create_classes)
cursor.execute(create_students)
cursor.execute(create_homework)
cursor.execute(insert_classes)
cursor.execute(insert_students)
cursor.execute(insert_homework)
connection.commit()

cursor.execute(check_setting)
print("PRAGMA foreign_keys with get_connection():", cursor.fetchone()[0])


def show(title, statement):
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


print()
show("Students and their classes", read_students)

print()
show("Homework before any delete", read_homework)

print("\nTry to put a student in class 99 (it does not exist)")
try:
    cursor.execute(bad_insert)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

print("\nTry to delete class 1 (Asha is still in it)")
try:
    cursor.execute(bad_delete)
except sqlite3.IntegrityError as error:
    print("Rejected:", error)

print("\nDelete the spare class 3 (nobody is in it)")
cursor.execute(delete_spare_class)
print("Classes deleted:", cursor.rowcount)
connection.commit()

print()
show("Homework after the delete (the class 3 homework went with it)", read_homework)

connection.close()

print("\nThe same bad insert with a plain sqlite3.connect()")
plain = sqlite3.connect(DATABASE_PATH)
plain_cursor = plain.cursor()
plain_cursor.execute(check_setting)
print("PRAGMA foreign_keys with a plain connect:", plain_cursor.fetchone()[0])
plain_cursor.execute(bad_insert)
print("Accepted! Nothing checked whether class 99 exists.")
plain.rollback()       # undo it, so the bad row never stays
plain.close()