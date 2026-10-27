-- Lesson 4 of 7 | Show Indexes
-- SQLite has no SHOW INDEXES command. It keeps a list of every index in sqlite_master and in the PRAGMA commands.
-- Indexes named sqlite_autoindex are built automatically for UNIQUE rules.
-- Indexes named idx are the ones we created ourselves.
-- In the origin column, c means CREATE INDEX, u means a UNIQUE rule, and pk means a PRIMARY KEY.

SELECT name, tbl_name
FROM sqlite_master
WHERE type = 'index'
ORDER BY tbl_name, name;

SELECT name AS index_name, "unique" AS is_unique, origin
FROM pragma_index_list('pupils')
ORDER BY name;

PRAGMA index_info(idx_pupils_marks);

SELECT sql
FROM sqlite_master
WHERE type = 'index'
  AND name = 'idx_pupils_marks';