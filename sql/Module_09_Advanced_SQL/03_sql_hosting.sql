-- Lesson 3 of 20 | SQL Hosting (SQLite version)
-- Big databases such as MySQL run on a server, and your program connects to it. That is hosting.
-- SQLite has no server. The whole database is one ordinary file that lives next to your program.
-- PRAGMA commands read and change the settings of that file.
-- WAL mode lets many readers work while one writer writes, which web apps often want.

PRAGMA journal_mode;

PRAGMA page_size;

PRAGMA encoding;

PRAGMA integrity_check;

PRAGMA journal_mode = WAL;

PRAGMA journal_mode = DELETE;