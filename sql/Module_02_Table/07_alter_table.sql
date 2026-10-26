-- Lesson 7 of 10 | Alter Table
-- ALTER TABLE changes the shape of a table that already holds data.
-- A new column starts empty (NULL), or with its DEFAULT value if it has one.

ALTER TABLE employees ADD COLUMN phone TEXT;

ALTER TABLE employees ADD COLUMN is_active INTEGER NOT NULL DEFAULT 1;

SELECT emp_id, name, phone, is_active
FROM employees
ORDER BY emp_id;

ALTER TABLE employees RENAME COLUMN phone TO mobile;

ALTER TABLE employees DROP COLUMN mobile;

PRAGMA table_info(employees);

-- The next statement is REJECTED ON PURPOSE.
-- SQLite cannot change the type of an existing column. Other databases can.

ALTER TABLE employees ALTER COLUMN salary TYPE INTEGER;