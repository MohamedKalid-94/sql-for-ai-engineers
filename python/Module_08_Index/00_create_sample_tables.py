import sqlite3
from config import DATABASE_PATH, read_statements

(create_table, fill_table, count_rows,
 first_rows, rows_per_city) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(fill_table)
connection.commit()
print("Table pupils created and filled with generated rows")


def show(title, statement):
    print(f"\n{title}")
    print("-" * len(title))
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(row)


show("How many pupils", count_rows)
show("The first three pupils", first_rows)
show("Pupils in each city", rows_per_city)

connection.close()