"""
WARNING:
This script deletes all records from tables.
The table structure remains.
Use only for learning/reset purposes.
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

    try:

        cursor.execute(f"DELETE FROM {table}")

        print(f"{table} -> Data Deleted Successfully")

    except sqlite3.OperationalError:

        print(f"{table} -> Table Not Found")

connection.commit()
connection.close()

print("\nAll table data deleted successfully.")