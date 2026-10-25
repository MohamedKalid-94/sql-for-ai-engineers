# Module 06: SQL Joins

## Overview

SQL JOIN is used to combine data from multiple tables based on a related column.

Joins are important for AI Engineers because AI applications usually store data across multiple tables:

- Users
- Projects
- Documents
- Chat History
- AI Agents
- Permissions
- Metadata

---

# Database Tables Used

## employees Table

| Column | Description |
|---|---|
| emp_id | Employee ID |
| name | Employee Name |
| email | Employee Email |
| salary | Employee Salary |
| dept_id | Department ID |
| manager_id | Manager Reference |


## departments Table

| Column | Description |
|---|---|
| dept_id | Department ID |
| department_name | Department Name |


## projects Table

| Column | Description |
|---|---|
| project_id | Project ID |
| project_name | Project Name |
| emp_id | Employee Reference |


---

# Topics Covered

## 01. USING JOIN
Combines tables using the same column name.

## 02. INNER JOIN
Returns only matching records from both tables.

## 03. LEFT JOIN
Returns all records from the left table and matching records from the right table.

## 04. RIGHT JOIN
SQLite does not directly support RIGHT JOIN.

## 05. CROSS JOIN
Returns Cartesian product.
Every row from first table combines with every row from second table.

## 06. FULL JOIN
Returns all records from both tables.
SQLite does not support FULL JOIN directly.

## 07. SELF JOIN
A table joined with itself.

## 08. DELETE JOIN
Deletes records based on another table condition.

## 09. UPDATE JOIN
Updates records using another table.

## 10. LEFT JOIN vs RIGHT JOIN
LEFT JOIN	                    RIGHT JOIN
Keeps all left table records	Keeps all right table records
Most commonly used	            Less commonly used
Supported in SQLite	            Implemented using LEFT JOIN

## 11. UNION vs JOIN
UNION
Combines rows from multiple queries.

JOIN
Combines columns from multiple tables.

Difference:
UNION	                        JOIN
Combines rows	                Combines columns
Same column structure required	Related column required

Technology:
Python
SQLite3

Execution:
python run_module.py

Output:
outputs/
└── Module_06_Joins/
    └── output.txt

Project Structure
Module_06_Joins
│
├── 00_insert_join_sample_data.py
├── 01_using_joins.py
├── 02_inner_join.py
├── 03_left_join.py
├── 04_right_join.py
├── 05_cross_join.py
├── 06_full_join.py
├── 07_self_join.py
├── 08_delete_join.py
├── 09_update_join.py
├── 10_left_join_vs_right_join.py
└── 11_union_vs_join.py

AI Engineering Connection
SQL JOIN concepts are used in:
RAG Applications
Example:
Users
 |
Projects
 |
Documents
 |
Document Metadata
 |
Embeddings
 |
Vector Database
 |
LLM

Agentic AI Systems
JOIN helps store and retrieve:
- Agent information
- Tasks
- Tool execution history
- User permissions
- Conversation memory