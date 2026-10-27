import sqlite3
from config import DATABASE_PATH, read_statements

list_all, list_pupils, index_info, index_sql = read_statements(__file__)

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

print("All indexes in this database")
print("----------------------------")
cursor.execute(list_all)
for index_name, table_name in cursor.fetchall():
    print(f"  {index_name:<32} on {table_name}")

print("\nIndexes on the pupils table (origin c = CREATE INDEX)")
print("-----------------------------------------------------")
cursor.execute(list_pupils)
for index_name, is_unique, origin in cursor.fetchall():
    print(f"  {index_name:<20} unique: {is_unique} | origin: {origin}")

print("\nColumns inside idx_pupils_marks")
print("-------------------------------")
cursor.execute(index_info)
for position, column_id, column_name in cursor.fetchall():
    print(f"  position {position}: column '{column_name}'")

print("\nThe command that built it, as SQLite stored it")
print("----------------------------------------------")
cursor.execute(index_sql)
print(" ", cursor.fetchone()[0])

connection.close()