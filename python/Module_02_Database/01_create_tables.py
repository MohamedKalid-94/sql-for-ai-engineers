import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


# Enable Foreign Key support in SQLite
cursor.execute("""
PRAGMA foreign_keys = ON;
""")


# ============================
# Create Departments Table
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments(

    dept_id INTEGER PRIMARY KEY,

    department_name TEXT NOT NULL UNIQUE

)
""")

print("Departments table created successfully")


# ============================
# Create Employees Table
# ============================

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(

    emp_id INTEGER PRIMARY KEY,

    name TEXT NOT NULL,

    email TEXT UNIQUE,

    salary REAL CHECK(salary >= 0),

    dept_id INTEGER,

    FOREIGN KEY(dept_id)
        REFERENCES departments(dept_id)

)
""")

print("Employees table created successfully")


# ============================
# Create Projects Table
# Avoid recreating after rename
# ============================


cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
AND name IN ('projects','company_projects')
""")


project_tables = [
    row[0]
    for row in cursor.fetchall()
]


if "projects" not in project_tables and "company_projects" not in project_tables:

    cursor.execute("""
    CREATE TABLE projects(

        project_id INTEGER PRIMARY KEY,

        project_name TEXT NOT NULL,

        emp_id INTEGER,

        FOREIGN KEY(emp_id)
            REFERENCES employees(emp_id)

    )
    """)

    print("Projects table created successfully")


elif "company_projects" in project_tables:

    print("Projects table already renamed to company_projects")


else:

    print("Projects table already exists")


connection.commit()

connection.close()