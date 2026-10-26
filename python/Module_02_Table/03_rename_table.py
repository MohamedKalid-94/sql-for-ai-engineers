import sqlite3
from config import DATABASE_PATH, read_statements

create_table, insert_rows, list_tables, rename_table, read_rows = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(create_table)
cursor.execute(insert_rows)
connection.commit()


def show_tables(title):
    print(title)
    cursor.execute(list_tables)
    for (name,) in cursor.fetchall():
        print("  ", name)


show_tables("Tables before the rename")

cursor.execute(rename_table)
connection.commit()

show_tables("\nTables after the rename")

print("\nRows are still there")
cursor.execute(read_rows)
for row in cursor.fetchall():
    print(row)

connection.close()