# Module 09 – Advanced SQL

## Objective

This module covers advanced SQL concepts that are commonly used in real-world database development and AI application backends. Since SQLite does not support some enterprise SQL features (such as Stored Procedures, Sequences, and Cursors), equivalent SQLite implementations are demonstrated wherever applicable.

---

# Topics Covered

| No | Topic | Status |
|----|----------------------------|--------|
| 00 | Create Sample Tables | ✅ |
| 01 | Wildcards | ✅ |
| 02 | SQL Injection | ✅ |
| 03 | SQL Hosting | ✅ |
| 04 | MIN & MAX | ✅ |
| 05 | NULL Functions | ✅ |
| 06 | CHECK Constraint | ✅ |
| 07 | DEFAULT Constraint | ✅ |
| 08 | Stored Procedures (SQLite Equivalent) | ✅ |
| 09 | NULL Values | ✅ |
| 10 | Transactions | ✅ |
| 11 | Sub Queries | ✅ |
| 12 | Handling Duplicates | ✅ |
| 13 | Sequences (SQLite Equivalent) | ✅ |
| 14 | AUTO INCREMENT | ✅ |
| 15 | Date & Time Functions | ✅ |
| 16 | Cursors (SQLite Equivalent) | ✅ |
| 17 | Common Table Expression (CTE) | ✅ |
| 18 | GROUP BY vs ORDER BY | ✅ |
| 19 | IN vs EXISTS | ✅ |
| 20 | Database Tuning | ✅ |

---

# Folder Structure

```
Module_09_Advanced_SQL/

SQL
├── 00_create_sample_tables.sql
├── 01_wildcards.sql
├── 02_sql_injection.sql
├── 03_sql_hosting.sql
├── 04_min_max.sql
├── 05_null_functions.sql
├── 06_check_constraint.sql
├── 07_default_constraint.sql
├── 08_stored_procedures.sql
├── 09_null_values.sql
├── 10_transactions.sql
├── 11_sub_queries.sql
├── 12_handling_duplicates.sql
├── 13_sequences.sql
├── 14_auto_increment.sql
├── 15_date_time.sql
├── 16_cursors.sql
├── 17_common_table_expression.sql
├── 18_group_by_vs_order_by.sql
├── 19_in_vs_exists.sql
└── 20_database_tuning.sql

Python
├── 00_create_sample_tables.py
├── 01_wildcards.py
├── 02_sql_injection.py
├── 03_sql_hosting.py
├── 04_min_max.py
├── 05_null_functions.py
├── 06_check_constraint.py
├── 07_default_constraint.py
├── 08_stored_procedures.py
├── 09_null_values.py
├── 10_transactions.py
├── 11_sub_queries.py
├── 12_handling_duplicates.py
├── 13_sequences.py
├── 14_auto_increment.py
├── 15_date_time.py
├── 16_cursors.py
├── 17_common_table_expression.py
├── 18_group_by_vs_order_by.py
├── 19_in_vs_exists.py
└── 20_database_tuning.py
```

---

# Key Learnings

## Wildcards

- `%`
- `_`

---

## SQL Injection

- Unsafe SQL
- Parameterized Queries
- Prepared Statements

---

## Aggregate Functions

- MIN()
- MAX()

---

## NULL Functions

- COALESCE()
- IFNULL()
- NULLIF()

---

## Constraints

- CHECK
- DEFAULT

---

## SQLite Equivalents

SQLite does not support:

- Stored Procedures
- Sequences
- Cursors

Equivalent implementations are provided using Python and SQLite.

---

## Transactions

- BEGIN
- COMMIT
- ROLLBACK

---

## Sub Queries

- Scalar Subquery
- Nested Query

---

## Handling Duplicates

- DISTINCT
- GROUP BY

---

## Date & Time

- DATE()
- TIME()
- DATETIME()

---

## Common Table Expression (CTE)

- WITH clause
- Temporary result sets

---

## Query Comparison

- GROUP BY vs ORDER BY
- IN vs EXISTS

---

## Database Tuning

SQLite query optimization using:

- EXPLAIN QUERY PLAN

---

# Execution

Run using:

```
python run_module.py
```

Output:

```
outputs/
└── Module_09_Advanced_SQL/
    └── output.txt
```

---

# Module Status

**Completed ✅**