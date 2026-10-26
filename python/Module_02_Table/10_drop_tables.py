import sqlite3
from config import DATABASE_PATH, read_statements

list_tables, drop_table, drop_if_exists, drop_missing = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


def show_tables(title):
    print(title)
    cursor.execute(list_tables)
    for (name,) in cursor.fetchall():
        print("  ", name)


show_tables("Tables before DROP")

cursor.execute(drop_table)
connection.commit()
show_tables("\nTables after DROP TABLE employees_copy")

cursor.execute(drop_if_exists)
print("\nDROP TABLE IF EXISTS on a missing table: no error")

try:
    cursor.execute(drop_missing)
except sqlite3.OperationalError as error:
    print("DROP TABLE on a missing table: rejected ->", error)

connection.close()