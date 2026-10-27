import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, insert_valid, read_rows, bad_price,
 bad_stock, bad_name, bad_update) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_valid)
connection.commit()


def show_rows(title):
    print(title)
    print("-" * len(title))
    cursor.execute(read_rows)
    for row in cursor.fetchall():
        print(row)


show_rows("Products that pass every rule")

print("\nRows that break a rule")
print("----------------------")
rejected = [
    ("Price of 0", bad_price),
    ("Negative stock", bad_stock),
    ("Name shorter than 3 letters", bad_name),
    ("Update to a negative price", bad_update),
]
for title, statement in rejected:
    try:
        cursor.execute(statement)
        print(f"{title:<28}: unexpectedly accepted")
    except sqlite3.IntegrityError as error:
        print(f"{title:<28}: rejected -> {error}")

print()
show_rows("Products after all attempts (nothing bad got in)")

connection.close()