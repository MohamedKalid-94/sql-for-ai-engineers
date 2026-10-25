"""
WARNING:
This script permanently deletes tables.
Use only when resetting the database.
"""

import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

tables = [
    "company_projects",
    "employees_backup",
    "employee_constraints",
    "employees",
    "departments"
]

for table in tables:

    cursor.execute(f"DROP TABLE IF EXISTS {table}")

    print(f"{table} -> Dropped Successfully")

connection.commit()
connection.close()

print("\nAll tables dropped successfully.")