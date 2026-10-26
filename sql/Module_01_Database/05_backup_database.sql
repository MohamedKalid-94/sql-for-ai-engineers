-- Lesson 5 of 6 | Backup Database
-- Way 1 (SQL): VACUUM INTO writes a clean copy of the database to a new file.
-- Way 2 (Python): connection.backup() copies it page by page, see the .py file.
-- The ? stands for the new file name, which Python supplies.

VACUUM INTO ?;

SELECT COUNT(*) FROM database_info;