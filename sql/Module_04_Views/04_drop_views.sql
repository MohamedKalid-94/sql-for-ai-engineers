-- Lesson 4 of 4 | Drop Views
-- DROP VIEW deletes the saved question only. The table and its data are never touched.

SELECT name
FROM sqlite_master
WHERE type = 'view'
ORDER BY name;

DROP VIEW employee_directory;

-- IF EXISTS makes the command safe when the view is already gone.

DROP VIEW IF EXISTS employee_directory;

-- The next statement is REJECTED ON PURPOSE.
-- The view no longer exists, so there is nothing to drop.

DROP VIEW employee_directory;

SELECT COUNT(*) AS employees_still_in_table
FROM employees;