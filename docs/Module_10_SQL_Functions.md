# Module 10 – SQL Functions

## Overview

SQL Functions are built-in functions used to manipulate and process data.

This module covers the most commonly used SQL functions along with their SQLite equivalents in Python.

---

## Topics Covered

| No | Topic | SQL File | Python File |
|----|---------|----------|-------------|
|00|Create Sample Tables|✅|✅|
|01|Date Functions|✅|✅|
|02|String Functions|✅|✅|
|03|Aggregate Functions|✅|✅|
|04|Numeric Functions|✅|✅|
|05|Text & Image Functions|✅|✅|
|06|Statistical Functions|✅|✅|
|07|Logical Functions|✅|✅|
|08|Cursor Functions|✅|✅|
|09|JSON Functions|✅|✅|
|10|Conversion Functions|✅|✅|
|11|Datatype Functions|✅|✅|

---

# Files

```
Module_10_SQL_Functions

SQL
│
├──00_create_sample_tables.sql
├──01_date_functions.sql
├──02_string_functions.sql
├──03_aggregate_functions.sql
├──04_numeric_functions.sql
├──05_text_image_functions.sql
├──06_statistical_functions.sql
├──07_logical_functions.sql
├──08_cursor_functions.sql
├──09_json_functions.sql
├──10_conversion_functions.sql
└──11_datatype_functions.sql

Python

├──00_create_sample_tables.py
├──01_date_functions.py
├──02_string_functions.py
├──03_aggregate_functions.py
├──04_numeric_functions.py
├──05_text_image_functions.py
├──06_statistical_functions.py
├──07_logical_functions.py
├──08_cursor_functions.py
├──09_json_functions.py
├──10_conversion_functions.py
└──11_datatype_functions.py
```

---

# Concepts Learned

## Date Functions

- DATE()
- TIME()
- DATETIME()
- Current Date
- Current Time

---

## String Functions

- UPPER()
- LOWER()
- LENGTH()
- SUBSTR()

---

## Aggregate Functions

- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()

---

## Numeric Functions

- ROUND()
- ABS()
- CEIL Equivalent
- FLOOR Equivalent

---

## Text & Image Functions

SQLite stores images as BLOB.

Functions demonstrated:

- LENGTH()
- SUBSTR()

---

## Statistical Functions

Using Aggregate Functions to calculate:

- Count
- Minimum
- Maximum
- Average
- Total

---

## Logical Functions

Using

- CASE
- WHEN
- THEN
- ELSE

---

## Cursor Functions

SQLite does not support SQL Server Cursor Functions.

Python cursor iteration is used as an equivalent.

---

## JSON Functions

SQLite JSON1 Extension

Functions demonstrated:

- json_object()

---

## Conversion Functions

Using

- CAST()

Convert

- Integer
- Text
- Real

---

## Datatype Functions

Using

```
typeof()
```

to identify

- INTEGER
- TEXT
- REAL
- NULL

---

# Execution Order

```
00_create_sample_tables.py

01_date_functions.py

02_string_functions.py

03_aggregate_functions.py

04_numeric_functions.py

05_text_image_functions.py

06_statistical_functions.py

07_logical_functions.py

08_cursor_functions.py

09_json_functions.py

10_conversion_functions.py

11_datatype_functions.py
```

---

# Learning Outcome

After completing this module, you will understand

- SQL built-in functions
- Date manipulation
- String manipulation
- Aggregate calculations
- Numeric operations
- JSON handling
- Type conversion
- SQLite datatype inspection
- Python sqlite3 equivalents

---

**Module Status**

Completed

```
12 SQL Examples
12 Python Examples

Total Files : 24
```