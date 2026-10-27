-- Lesson 6 of 6 | Keys in the Real Tables
-- SQLite stores every key we make and can show it to us with PRAGMA commands.
-- Here we look at the shared employees table, which the runner built from sql/common/schema.sql.
-- table_info shows the primary key. index_list shows the UNIQUE keys. foreign_key_list shows the foreign keys.

PRAGMA table_info(employees);

PRAGMA index_list(employees);

PRAGMA foreign_key_list(employees);