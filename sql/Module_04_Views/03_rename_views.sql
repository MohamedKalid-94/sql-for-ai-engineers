-- Lesson 3 of 4 | Rename Views (SQLite equivalent)
-- SQLite has no ALTER VIEW ... RENAME. To rename a view:
-- 1) create a new view with the new name and the same question
-- 2) drop the old view

SELECT name
FROM sqlite_master
WHERE type = 'view'
ORDER BY name;

CREATE VIEW employee_directory AS
SELECT e.emp_id, e.name, e.salary, d.dept_name
FROM employees AS e
JOIN departments AS d ON d.dept_id = e.dept_id;

DROP VIEW employee_details;

SELECT emp_id, name, dept_name
FROM employee_directory
ORDER BY emp_id;

-- The next statement is REJECTED ON PURPOSE.
-- SQLite cannot rename a view with ALTER.

ALTER VIEW employee_directory RENAME TO staff_directory;