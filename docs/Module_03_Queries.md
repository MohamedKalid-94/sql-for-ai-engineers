# Module 03 - SQL Queries

## Objective

Learn the fundamental SQL Data Manipulation Language (DML) operations using SQL and their equivalent implementation in Python (`sqlite3`).

This module demonstrates how to insert, retrieve, copy, update, delete, and sort data in a relational database.

---

## Topics Covered

1. Insert Sample Data
2. INSERT Query
3. SELECT Query
4. SELECT INTO (SQLite Equivalent)
5. INSERT INTO SELECT
6. UPDATE Query
7. DELETE Query
8. ORDER BY (Sorting Results)

---

## Folder Structure

```
Module_03_Database

SQL
│
├── 00_insert_sample_data.sql
├── 01_insert_query.sql
├── 02_select_query.sql
├── 03_select_into.sql
├── 04_insert_into_select.sql
├── 05_update_query.sql
├── 06_delete_query.sql
├── 07_sorting_results.sql
├── 98_delete_query_data.sql
└── 99_drop_query_tables.sql

Python
│
├── 00_insert_sample_data.py
├── 01_insert_query.py
├── 02_select_query.py
├── 03_select_into.py
├── 04_insert_into_select.py
├── 05_update_query.py
├── 06_delete_query.py
├── 07_sorting_results.py
├── 98_delete_query_data.py
└── 99_drop_query_tables.py
```

---

# Concepts Learned

## 1. INSERT

Adds new records into a table.

Example

```sql
INSERT INTO employees
(emp_id,name,email,salary,dept_id)
VALUES
(111,'Robert','robert@gmail.com',76000,4);
```

---

## 2. SELECT

Retrieves data from a table.

Example

```sql
SELECT *
FROM employees;
```

---

## 3. SELECT INTO (SQLite Equivalent)

SQLite does not support SQL Server's `SELECT INTO`.

Equivalent:

```sql
CREATE TABLE employee_copy AS

SELECT *

FROM employees;
```

---

## 4. INSERT INTO SELECT

Copies data from one table into another.

Example

```sql
INSERT INTO employees_backup

SELECT *

FROM employees;
```

---

## 5. UPDATE

Modifies existing records.

Example

```sql
UPDATE employees

SET salary = 75000

WHERE emp_id = 101;
```

---

## 6. DELETE

Removes records from a table.

Example

```sql
DELETE

FROM employees

WHERE emp_id = 111;
```

---

## 7. ORDER BY

Sorts query results.

Ascending

```sql
SELECT *
FROM employees
ORDER BY salary ASC;
```

Descending

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

---

# Python Concepts

This module demonstrates:

- sqlite3
- connect()
- cursor()
- execute()
- executemany()
- fetchall()
- commit()
- close()

---

# Execution Order

```
00_insert_sample_data.py
        ↓
01_insert_query.py
        ↓
02_select_query.py
        ↓
03_select_into.py
        ↓
04_insert_into_select.py
        ↓
05_update_query.py
        ↓
06_delete_query.py
        ↓
07_sorting_results.py
```

Cleanup scripts are available but excluded from the normal execution.

```
98_delete_query_data.py
99_drop_query_tables.py
```

These scripts can be executed manually whenever database cleanup or reset is required.

---

# Output

Execute the module using

```bash
python run_module.py
```

Generated output

```
outputs/
└── Module_03_Database/
    └── output.txt
```

---

# Learning Outcome

After completing this module, you will be able to:

- Insert records into a table
- Retrieve records using SELECT
- Create a table from an existing table
- Copy records between tables
- Update existing data
- Delete records
- Sort query results
- Perform SQL operations using Python (`sqlite3`)

---

# Status

✅ Module 03 Completed