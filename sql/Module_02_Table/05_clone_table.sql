-- Lesson 5 of 10 | Clone Table
-- CREATE TABLE ... AS SELECT photocopies a table.
-- WHERE 1 = 0 is never true, so that copy has the columns but no rows.
-- A clone copies the columns and the data, but NOT the rules such as PRIMARY KEY.

CREATE TABLE employees_copy AS
SELECT * FROM employees;

CREATE TABLE employees_empty_copy AS
SELECT * FROM employees
WHERE 1 = 0;

SELECT 'employees' AS table_name, COUNT(*) AS row_count FROM employees
UNION ALL
SELECT 'employees_copy', COUNT(*) FROM employees_copy
UNION ALL
SELECT 'employees_empty_copy', COUNT(*) FROM employees_empty_copy;

PRAGMA table_info(employees);

PRAGMA table_info(employees_copy);