-- Lesson 2 of 4 | Update Views (SQLite equivalent)
-- Updating a view can mean two things.
-- 1) Changing the DATA through the view. SQLite views are read-only, so change the table instead.
-- 2) Changing the DEFINITION of the view. SQLite has no ALTER VIEW and no CREATE OR REPLACE VIEW.
--    The SQLite way is DROP VIEW, then CREATE VIEW again with the new question.

SELECT emp_id, name, salary
FROM high_salary_employees
ORDER BY emp_id;

-- The next statement is REJECTED ON PURPOSE.
-- A view has no data of its own to change.

UPDATE high_salary_employees
SET salary = 1
WHERE emp_id = 102;

DROP VIEW high_salary_employees;

CREATE VIEW high_salary_employees AS
SELECT emp_id, name, email, salary, dept_id
FROM employees
WHERE salary >= 75000;

SELECT emp_id, name, email, salary
FROM high_salary_employees
ORDER BY emp_id;

-- The next statement is REJECTED ON PURPOSE.
-- This is how other databases replace a view, but SQLite does not understand it.

CREATE OR REPLACE VIEW high_salary_employees AS
SELECT emp_id, name
FROM employees;

SELECT sql
FROM sqlite_master
WHERE type = 'view'
  AND name = 'high_salary_employees';