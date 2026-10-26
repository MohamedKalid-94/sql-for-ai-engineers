import os
import sqlite3
from config import DATABASE_PATH, RENAMED_DATABASE_PATH, read_statements

(read_info,) = read_statements(__file__)

if not DATABASE_PATH.exists():
    raise SystemExit("Database not found. Run lessons 01 to 03 first.")

# os.replace overwrites an old leftover file, so a rerun never fails
os.replace(DATABASE_PATH, RENAMED_DATABASE_PATH)
print(f"Renamed: {DATABASE_PATH.name} -> {RENAMED_DATABASE_PATH.name}")
print("Old name exists:", DATABASE_PATH.exists())
print("New name exists:", RENAMED_DATABASE_PATH.exists())

connection = sqlite3.connect(RENAMED_DATABASE_PATH)
try:
    cursor = connection.cursor()
    print("\nData read through the new name")
    print("------------------------------")
    cursor.execute(read_info)
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
    # put the old name back, even if something above failed
    os.replace(RENAMED_DATABASE_PATH, DATABASE_PATH)

print(f"\nRenamed back: {RENAMED_DATABASE_PATH.name} -> {DATABASE_PATH.name}")