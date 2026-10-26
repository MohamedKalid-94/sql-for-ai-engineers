-- Lesson 2 of 6 | Show Databases
-- SQLite's version of SHOW DATABASES is PRAGMA database_list.
-- Each row shows: a number, the database name, and the file it lives in.
-- A database kept only in memory has no file.

PRAGMA database_list;

ATTACH DATABASE ':memory:' AS scratch;

PRAGMA database_list;