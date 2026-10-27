-- Lesson 8 of 20 | Stored Procedures (SQLite equivalent)
-- SQL Server saves a routine inside the database with CREATE PROCEDURE. SQLite cannot.
-- The SQLite way is to keep the routine as a Python function that sends named parameters
-- (:dept, :min_salary and so on) to a saved query.
-- Python can also register a function that SQL itself can call, such as income_tax below.

SELECT emp_id, name, salary
FROM employees
WHERE dept_id = :dept
  AND salary >= :min_salary
ORDER BY emp_id;

UPDATE employees
SET salary = ROUND(salary * (1 + :percent / 100.0), 2)
WHERE dept_id = :dept;

SELECT name, salary, income_tax(salary) AS tax
FROM employees
ORDER BY emp_id;