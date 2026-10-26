-- Lesson 9 of 10 | Delete Table Data
-- DELETE removes rows but keeps the table itself. Always check the WHERE part.
-- A change is not permanent until we commit it, so a rollback can undo it.

SELECT COUNT(*) AS rows_in_employees FROM employees;

DELETE FROM employees WHERE dept_id = 5;

DELETE FROM employees;