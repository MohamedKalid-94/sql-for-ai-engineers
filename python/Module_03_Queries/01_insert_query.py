import sqlite3
from config import DATABASE_PATH, read_statements

insert_one, insert_many, insert_placeholder, read_new = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(insert_one)
print("Way 1, one row    :", cursor.rowcount, "row inserted")

cursor.execute(insert_many)
print("Way 2, many rows  :", cursor.rowcount, "rows inserted")

new_people = [
    (111, "Ravi", "ravi@gmail.com", 77000, 2),
    (112, "Tina", "tina@gmail.com", 58000, 4),
]
cursor.executemany(insert_placeholder, new_people)
print("Way 3, with ?     :", cursor.rowcount, "rows inserted")

connection.commit()

print("\nThe five new employees (phone is NULL, is_active got its DEFAULT)")
print("-----------------------------------------------------------------")
cursor.execute(read_new)
for row in cursor.fetchall():
    print(row)

connection.close()