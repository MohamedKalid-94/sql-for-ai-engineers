-- Lesson 16 of 20 | Cursors (SQLite equivalent)
-- In SQL Server, DECLARE CURSOR walks through rows one at a time inside the database.
-- SQLite has no such command. The Python cursor does the same job:
-- fetchone gives one row, fetchmany gives a few, fetchall gives the rest, and a for loop walks them all.
-- Row-by-row work is slower than a single set-based command, so use it only when you must.

SELECT emp_id, name, salary
FROM employees
ORDER BY emp_id;

UPDATE employees
SET salary = :new_salary
WHERE emp_id = :emp_id;

UPDATE employees
SET salary = ROUND(salary * 1.05, 2);