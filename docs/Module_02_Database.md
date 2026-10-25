# Module 02 - SQL Tables

## Objective

Learn how to create, modify, manage, and remove tables using SQL and Python (`sqlite3`).

---

## Topics Covered

1. Create Table
2. Show Tables
3. Rename Table
4. Truncate Table (SQLite uses DELETE)
5. Clone Table
6. Temporary Table
7. Alter Table
8. Constraints
9. Delete Table Data
10. Drop Tables

---

## Folder Structure

```
Module_02_Database

SQL
│
├── 01_create_tables.sql
├── 02_show_tables.sql
├── 03_rename_table.sql
├── 04_truncate_table.sql
├── 05_clone_table.sql
├── 06_temporary_table.sql
├── 07_alter_table.sql
├── 08_constraints.sql
├── 98_delete_table_data.sql
└── 99_drop_tables.sql

Python
│
├── 01_create_tables.py
├── 02_show_tables.py
├── 03_rename_table.py
├── 04_truncate_table.py
├── 05_clone_table.py
├── 06_temporary_table.py
├── 07_alter_table.py
├── 08_constraints.py
├── 98_delete_table_data.py
└── 99_drop_tables.py
```

---

## Concepts Learned

### CREATE TABLE
Creates new database tables.

### SHOW TABLES
Lists all tables in the SQLite database.

### RENAME TABLE
Renames an existing table.

### TRUNCATE TABLE
SQLite does not support `TRUNCATE TABLE`.

Equivalent:

```sql
DELETE FROM table_name;
```

---

### CLONE TABLE

Creates a duplicate table using

```sql
CREATE TABLE new_table AS
SELECT * FROM existing_table;
```

---

### TEMPORARY TABLE

Creates a table that exists only during the current database session.

---

### ALTER TABLE

Used to

- Add columns
- Rename tables
- Rename columns

---

### CONSTRAINTS

Implemented

- PRIMARY KEY
- FOREIGN KEY
- UNIQUE
- NOT NULL
- CHECK
- DEFAULT

---

### DELETE TABLE DATA

Deletes all records while preserving the table structure.

---

### DROP TABLE

Completely removes the table from the database.

---

## Python Concepts

- sqlite3
- CREATE TABLE
- ALTER TABLE
- CREATE TEMP TABLE
- DROP TABLE
- Transactions
- commit()
- close()

---

## Output

Generated automatically using

```
python run_module.py
```

Output location

```
outputs/
└── Module_02_Database/
    └── output.txt
```

---

## Status

✅ Completed