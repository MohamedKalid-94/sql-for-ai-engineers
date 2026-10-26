-- Lesson 8 of 11 | DELETE JOIN (SQLite equivalent)
-- MySQL and SQL Server can write DELETE ... JOIN. SQLite cannot.
-- The SQLite way is DELETE FROM table WHERE ... with a subquery that does the matching.
-- Delete 1: remove every employee whose department is GenAI.
-- Delete 2: remove every employee who has no matching department at all.
-- We do not save the deletes. A rollback at the end puts everyone back.

SELECT e.emp_id, e.name, d.dept_name
FROM employees AS e
LEFT JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY e.emp_id;

DELETE FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE dept_name = 'GenAI');

DELETE FROM employees
WHERE NOT EXISTS (SELECT 1 FROM departments AS d WHERE d.dept_id = employees.dept_id);

SELECT emp_id, name, dept_id
FROM employees
ORDER BY emp_id;