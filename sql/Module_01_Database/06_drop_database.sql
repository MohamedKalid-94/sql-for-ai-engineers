-- Lesson 6 of 6 | Drop Database
-- DETACH takes an attached database off the desk. The data is not lost.
-- Dropping a database for real means deleting its file, which Python does.

ATTACH DATABASE ':memory:' AS scratch;

PRAGMA database_list;

DETACH DATABASE scratch;

PRAGMA database_list;