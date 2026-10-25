"""
WARNING:
Deletes all records from Module 03 tables.
"""

import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

tables = [
    "company_projects",
    "employees",
    "departments"
]

for table in tables:

    cursor.execute(f"DELETE FROM {table}")

    print(f"{table} cleared")

connection.commit()

connection.close()

print("\nAll records deleted")