-- Lesson 4 of 11 | RIGHT JOIN
-- RIGHT JOIN keeps EVERY row of the right table (the one written second).
-- SQLite understands RIGHT JOIN from version 3.39 onwards.
-- On any SQLite version the same answer comes from swapping the two tables
-- and using LEFT JOIN instead.

SELECT d.dept_name, e.name
FROM employees AS e
RIGHT JOIN departments AS d ON d.dept_id = e.dept_id
ORDER BY d.dept_id, e.name;

SELECT d.dept_name, e.name
FROM departments AS d
LEFT JOIN employees AS e ON e.dept_id = d.dept_id
ORDER BY d.dept_id, e.name;

SELECT d.dept_name
FROM departments AS d
LEFT JOIN employees AS e ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL;