-- Lesson 1 of 6 | Create Database
-- SQLite has no CREATE DATABASE command.
-- A new database file is made the first time we connect and write to it.
-- Below we write the first page of the new notebook: a table called database_info.

CREATE TABLE database_info (
    info_id    INTEGER PRIMARY KEY,
    purpose    TEXT NOT NULL,
    created_by TEXT NOT NULL
);

INSERT INTO database_info (purpose, created_by)
VALUES ('Module 01 demo database', 'run_module.py');

SELECT info_id, purpose, created_by
FROM database_info;