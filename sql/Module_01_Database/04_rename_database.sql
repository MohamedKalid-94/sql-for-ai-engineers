-- Lesson 4 of 6 | Rename Database
-- Renaming a SQLite database means renaming its file.
-- Python does the renaming, because SQL cannot touch files.
-- This query proves the data is still inside after the rename.

SELECT purpose, created_by
FROM database_info;