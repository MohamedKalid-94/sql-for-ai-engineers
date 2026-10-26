-- Lesson 2 of 10 | Show Tables
-- SQLite keeps an index of all its tables in a built-in table called sqlite_master.
-- Names starting with sqlite_ are SQLite's own housekeeping tables, so we hide them.

SELECT name
FROM sqlite_master
WHERE type = 'table'
  AND name NOT LIKE 'sqlite_%'
ORDER BY name;

-- PRAGMA table_info is the SQLite version of DESCRIBE.
-- It lists the columns of one table.

PRAGMA table_info(employees);