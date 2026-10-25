# Module 07: SQL Keys 🔑

## Overview

SQL Keys are used to maintain data accuracy, uniqueness, and relationships between database tables.

In this module, SQL Key concepts are implemented using:

- SQLite Database
- Python sqlite3
- Practical examples

---

# Learning Objectives

After completing this module, you will understand:

- How to create UNIQUE constraints
- How Primary Keys identify records
- How Foreign Keys create relationships
- How Composite Keys work
- How Alternate Keys are used

---

# Technology Used

| Technology | Purpose |
|---|---|
| Python | Execute SQL operations |
| SQLite | Relational Database |
| SQL | Key constraints |

---

# Module Structure

```
Module_07_Keys/

│
├── 00_create_sample_tables.py
├── 01_unique_key.py
├── 02_primary_key.py
├── 03_foreign_key.py
├── 04_composite_key.py
└── 05_alternate_key.py
```

---

# 01. UNIQUE KEY

## Concept

A UNIQUE KEY ensures that all values in a column are different.

Example:

```sql
CREATE TABLE employees_unique (
    emp_id INTEGER,
    email TEXT UNIQUE
);
```

Purpose:

- Prevent duplicate values
- Maintain data integrity

Output:

```
(101, 'john@gmail.com')
(102, 'sara@gmail.com')
```

---

# 02. PRIMARY KEY

## Concept

A Primary Key uniquely identifies each record in a table.

Rules:

- Cannot contain NULL values
- Must contain unique values

Example:

```sql
CREATE TABLE employees_pk (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
);
```

Output:

```
(101, 'John', 75000.0)
(102, 'Sara', 85000.0)
```

---

# 03. FOREIGN KEY

## Concept

A Foreign Key creates a relationship between two tables.

Example:

Department Table:

```
department_id
department_name
```

Employee Table:

```
emp_id
name
department_id
```

Relationship:

```
departments
      |
      |
department_id
      |
employees
```

SQL:

```sql
FOREIGN KEY(department_id)
REFERENCES departments(department_id)
```

Output:

```
('John','AI')
('Sara','Python')
```

---

# 04. COMPOSITE KEY

## Concept

A Composite Key is created using multiple columns together.

Example:

```sql
CREATE TABLE employee_projects (

    emp_id INTEGER,
    project_id INTEGER,

    PRIMARY KEY(emp_id, project_id)

);
```

Combination must be unique.

Valid:

```
(101,1)
(101,2)
(102,1)
```

Invalid:

```
(101,1)
(101,1) ❌
```

---

# 05. ALTERNATE KEY

## Concept

An Alternate Key is a candidate key that is not selected as the Primary Key.

Example:

```sql
CREATE TABLE users (

user_id INTEGER PRIMARY KEY,

username TEXT UNIQUE,

email TEXT UNIQUE

);
```

Here:

```
user_id  -> Primary Key

username -> Alternate Key

email    -> Alternate Key
```

Output:

```
(1,'kalid','kalid@gmail.com')
(2,'john','john@gmail.com')
```

---

# Execution

Run:

```bash
python run_module.py
```

Select:

```
Module_07_Keys
```

Output:

```
outputs/

└── Module_07_Keys/

    └── output.txt
```

---

# AI Engineering Connection 🤖

SQL Keys are important for AI application databases.

Used for:

- User management
- Document storage
- Chat history
- Agent workflows
- RAG metadata
- Permission management


Example:

```
Users
 |
 |
Documents
 |
 |
Embeddings
 |
 |
AI Retrieval System
```

Primary Keys identify records.

Foreign Keys connect AI application entities.

---

# Module Status

| Module | Status |
|---|---|
| SQL Keys | ✅ Completed |

---

# Author

Mohamed Kalid