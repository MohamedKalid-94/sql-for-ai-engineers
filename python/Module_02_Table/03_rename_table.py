import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

# Get all tables
cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

tables = [row[0] for row in cursor.fetchall()]

if "company_projects" in tables:
    print("Table already renamed.")

elif "projects" in tables:
    cursor.execute("""
    ALTER TABLE projects
    RENAME TO company_projects
    """)
    connection.commit()
    print("Table Renamed Successfully")

else:
    print("projects table not found.")

connection.close()