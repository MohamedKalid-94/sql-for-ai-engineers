-- Lesson 8 of 11 | Cursor Functions (SQLite equivalent)
-- A cursor is the pointer that walks through the rows of a result.
-- SQL Server has cursor commands such as OPEN, FETCH and CLOSE. SQLite has none of them.
-- The cursor lives in Python instead, and it has useful properties and methods.
-- Module 9 showed fetchone, fetchmany and fetchall. This lesson shows the rest of the cursor toolbox.
-- The question marks are filled in by Python.

SELECT emp_id, name, salary
FROM employees
ORDER BY emp_id;

UPDATE employees
SET salary = salary + 1000
WHERE dept_id = ?;

INSERT INTO departments (dept_name)
VALUES (?);

DELETE FROM departments
WHERE dept_name = ?;