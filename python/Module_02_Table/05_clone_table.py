import sqlite3
from config import DATABASE_PATH, read_statements

(clone_all, clone_structure, count_rows,
 describe_original, describe_copy) = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute(clone_all)
cursor.execute(clone_structure)
connection.commit()

print("Rows in each table")
print("------------------")
cursor.execute(count_rows)
for table_name, row_count in cursor.fetchall():
    print(f"{table_name:<22}: {row_count}")


def primary_key_columns(statement):
    cursor.execute(statement)
    return [row[1] for row in cursor.fetchall() if row[5]]


print("\nPrimary key columns")
print("-------------------")
print("employees     :", primary_key_columns(describe_original))
print("employees_copy:", primary_key_columns(describe_copy), "<- the clone lost its rules")

connection.close()