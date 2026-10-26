-- Lesson 1 of 24 | WHERE Clause
-- WHERE keeps only the rows that pass a test. Rows that fail are left out.
-- Text values go inside single quotes. Numbers do not.

SELECT emp_id, name, salary
FROM employees
WHERE salary > 80000
ORDER BY emp_id;

SELECT name, dept_id
FROM employees
WHERE dept_id = 1
ORDER BY name;

SELECT name, email
FROM employees
WHERE name = 'Alex';