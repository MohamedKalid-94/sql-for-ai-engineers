-- Lesson 6 of 7 | DELETE
-- DELETE removes rows. Good habit: run SELECT with the same WHERE first, to preview.
-- No WHERE means every row is removed, so keep a rollback ready.

SELECT COUNT(*) AS rows_in_employees
FROM employees;

DELETE FROM employees
WHERE emp_id = 112;

SELECT emp_id, name, salary
FROM employees
WHERE salary < 65000
ORDER BY emp_id;

DELETE FROM employees
WHERE salary < 65000;

DELETE FROM employees;