"""
WARNING:
Drops Module 03 temporary tables.
"""

import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS employee_copy")

print("employee_copy dropped")

connection.commit()

connection.close()

print("Temporary tables removed")