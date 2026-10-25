# Module 05: SQL Operators and Clauses 🚀

This module covers SQL operators and clauses used for filtering, sorting, grouping, conditional logic, NULL handling, and combining query results.

Implementation is done using:

- SQL
- Python
- SQLite Database


---

# 🎯 Learning Objectives

After completing this module, you will understand:

- Filtering records using SQL conditions
- Sorting and grouping data
- Applying logical operators
- Handling NULL values
- Using conditional expressions
- Combining multiple query results


---

# 📚 Topics Covered


## 01. WHERE Clause

Filter records based on conditions.

Example:

```sql
SELECT *
FROM employees
WHERE salary > 70000;
```


---

## 02. TOP Clause

SQLite equivalent:

```sql
LIMIT
```

Example:

```sql
SELECT *
FROM employees
LIMIT 5;
```


---

## 03. DISTINCT Clause

Removes duplicate values.

```sql
SELECT DISTINCT dept_id
FROM employees;
```


---

## 04. ORDER BY Clause

Sort query results.

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```


---

## 05. GROUP BY Clause

Groups records for aggregate operations.

```sql
SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id;
```


---

## 06. HAVING Clause

Filters grouped results.

```sql
SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id
HAVING AVG(salary)>70000;
```


---

## 07. AND & OR Operators

Combine multiple conditions.

```sql
SELECT *
FROM employees
WHERE salary > 70000
AND dept_id = 1;
```


---

## 08. BOOLEAN Operator

Used for TRUE/FALSE conditions.

SQLite uses:

```
0 = False
1 = True
```


---

## 09. LIKE Operator

Pattern matching.

```sql
SELECT *
FROM employees
WHERE name LIKE 'J%';
```


---

## 10. IN Operator

Multiple value comparison.

```sql
SELECT *
FROM employees
WHERE dept_id IN (1,2,3);
```


---

## 11. ANY / ALL Operators

SQLite equivalent using:

- MIN()
- MAX()
- Subqueries


---

## 12. EXISTS Operator

Checks whether records exist.

```sql
SELECT *
FROM employees e
WHERE EXISTS
(
SELECT 1
FROM departments d
WHERE d.dept_id=e.dept_id
);
```


---

## 13. CASE Expression

Conditional logic in SQL.

```sql
CASE
WHEN salary >=90000 THEN 'High'
ELSE 'Normal'
END
```


---

## 14. NOT Operator

Reverse conditions.

```sql
SELECT *
FROM employees
WHERE NOT dept_id=1;
```


---

## 15. NOT EQUAL Operator

Operators:

```
!=
<>
```


Example:

```sql
WHERE dept_id <> 1
```


---

## 16. IS NULL

Find missing values.

```sql
WHERE joining_date IS NULL
```


---

## 17. IS NOT NULL

Find available values.

```sql
WHERE joining_date IS NOT NULL
```


---

## 18. NOT NULL Constraint

Prevents empty values during insertion.


Example:

```sql
name TEXT NOT NULL
```


---

## 19. BETWEEN Operator

Range filtering.

```sql
WHERE salary BETWEEN 70000 AND 90000
```


---

## 20. UNION Operator

Combines results and removes duplicates.


---

## 21. UNION vs UNION ALL


| Operator | Duplicate |
|---|---|
| UNION | Removes duplicates |
| UNION ALL | Keeps duplicates |


---

## 22. INTERSECT Operator

Returns common records.


---

## 23. EXCEPT Operator

Returns records from first query but not second query.


---

## 24. Aliases

Temporary names for tables or columns.


Example:

```sql
SELECT
name AS employee_name
FROM employees;
```


---

# 📂 Module Structure


```
Module_05_Operators_and_Clauses

sql/

01_where_clause.sql
02_top_clause.sql
...
24_aliases.sql


python/

01_where_clause.py
02_top_clause.py
...
24_aliases.py
```


---

# 🤖 AI Engineering Connection


SQL operators are important for AI applications:


- Filtering user data
- Querying document metadata
- Managing AI conversations
- Searching application records
- Building backend APIs


Example RAG Application:


```
User Query

     |
     
FastAPI

     |

SQL Database

     |

Document Metadata

     |

Vector Database

     |

LLM
```


---

# ✅ Module Status

Completed:

- WHERE
- ORDER BY
- GROUP BY
- HAVING
- Operators
- NULL Handling
- Set Operators
- Aliases

