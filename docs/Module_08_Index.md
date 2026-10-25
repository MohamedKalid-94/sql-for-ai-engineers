# Module 08: SQL Indexes 🚀

## Overview

SQL Indexes are database optimization techniques used to improve query performance by allowing faster data retrieval.

This module covers index creation, management, and different types of indexes using SQLite + Python.

---

# 🎯 Learning Objectives

By completing this module, you will understand:

- What is an SQL Index
- Why indexes are required
- How indexes improve query performance
- Creating indexes
- Dropping indexes
- Viewing available indexes
- Unique indexes
- Clustered index concept
- Non-clustered index concept

---

# 🛠️ Technology Used

| Technology | Purpose |
|---|---|
| Python | Execute SQL operations |
| SQLite | Database engine |
| SQL | Index commands |
| sqlite3 | Python database connector |

---

# 📂 Module Structure


Module_08_Indexes/

│
├── 00_create_sample_tables.py
├── 01_indexes.py
├── 02_create_index.py
├── 03_drop_index.py
├── 04_show_indexes.py
├── 05_unique_index.py
├── 06_clustered_index.py
└── 07_non_clustered_index.py

---

# 📚 Topics Covered

## 01. SQL Indexes
An index is a database object that improves the speed of data retrieval.

## 02. Create Index

Purpose:
- Faster searching
- Faster filtering
- Improved query performance

## 03. Drop Index
Remove an existing index.

Syntax:
DROP INDEX index_name;

Example:
DROP INDEX idx_employee_salary;

## 04. Show Indexes
SQLite command:
PRAGMA index_list('employees');

Used to display indexes created on a table.

## 05. Unique Index
A unique index prevents duplicate values.

Example:
CREATE UNIQUE INDEX idx_unique_email
ON employees(email);

Use cases:
- Email addresses
- Usernames
- Employee codes

## 06. Clustered Index
A clustered index determines the physical storage order of data.

SQLite does not support traditional clustered indexes.

## 07. Non-Clustered Index
A non-clustered index stores indexed values separately with pointers to actual rows.

Use cases:
- Searching department-wise employees
- Filtering frequently used columns
🔗 AI Engineering Connection
Indexes are important in AI applications for:
- Faster user lookup
- Document metadata search
- Chat history retrieval
- Permission checking
- RAG application backend optimization

Example:
User Query
    |
FastAPI
    |
SQL Database
    |
Indexed Metadata
    |
Vector Search
    |
LLM Response


# ▶️ Execution
Run:
python run_module.py

Select:
Module_08_Indexes

Output:
outputs/
└── Module_08_Indexes/
    └── output.txt

✅ Module Status
Module	Status
SQL Indexes	✅ Completed

Author
Mohamed Kalid