-- Lesson 10 of 10 | Drop Tables
-- DROP TABLE removes the table and all of its data for good. There is no undo.

SELECT name
FROM sqlite_master
WHERE type = 'table'
  AND name NOT LIKE 'sqlite_%'
ORDER BY name;

DROP TABLE employees_copy;

-- IF EXISTS makes the command safe when the table is already gone.

DROP TABLE IF EXISTS employees_copy;

-- The next statement is REJECTED ON PURPOSE.
-- The table no longer exists, so there is nothing to drop.

DROP TABLE employees_copy;