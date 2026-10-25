# Module 04 - SQL Views

## Objective

Learn how to create, modify, remove, and rename SQL Views using SQL and their equivalent implementation in Python (`sqlite3`).

Views provide a virtual table that simplifies complex queries and improves data abstraction.

---

## Topics Covered

1. Create View
2. Update View (SQLite Equivalent)
3. Drop View
4. Rename View (SQLite Equivalent)

---

## Folder Structure

```
Module_04_Database

SQL
│
├── 01_create_view.sql
├── 02_update_view.sql
├── 03_drop_view.sql
└── 04_rename_view.sql

Python
│
├── 01_create_view.py
├── 02_update_view.py
├── 03_drop_view.py
└── 04_rename_view.py
```

---

# Concepts Learned

## CREATE VIEW

Creates a virtual table based on a SQL query.

Example

```sql
CREATE VIEW employee_details AS

SELECT
    e.emp_id,
    e.name,
    e.email,
    e.salary,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;
```

---

## UPDATE VIEW

SQLite does not support

```sql
CREATE OR REPLACE VIEW
```

Equivalent approach

1. Drop the existing view.
2. Create the view again with the updated definition.

---

## DROP VIEW

Removes an existing view from the database.

Example

```sql
DROP VIEW IF EXISTS employee_details;
```

---

## RENAME VIEW

SQLite does not support

```sql
ALTER VIEW view_name RENAME TO new_view_name;
```

Equivalent approach

1. Drop the old view.
2. Create a new view with the desired name.

---

# Python Concepts

This module demonstrates

- sqlite3
- connect()
- cursor()
- execute()
- commit()
- close()

---

# Execution Order

```
01_create_view.py
        ↓
02_update_view.py
        ↓
03_drop_view.py
        ↓
04_rename_view.py
```

---

# Output

Execute the module using

```bash
python run_module.py
```

Generated output

```
outputs/
└── Module_04_Database/
    └── output.txt
```

---

# Learning Outcome

After completing this module, you will be able to

- Create SQL Views
- Modify Views using the SQLite equivalent approach
- Drop Views
- Rename Views using the SQLite equivalent approach
- Access data through virtual tables
- Understand the advantages and limitations of SQL Views

---

# SQLite Notes

SQLite does not support:

- CREATE OR REPLACE VIEW
- ALTER VIEW ... RENAME TO

These operations are implemented by dropping and recreating the view.

---

# Status

✅ Module 04 Completed