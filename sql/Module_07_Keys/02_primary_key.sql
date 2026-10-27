-- Lesson 2 of 6 | PRIMARY KEY
-- A PRIMARY KEY is the one column that names each row, like a roll number in a class register.
-- It must be different for every row.
-- In SQLite, a column typed INTEGER PRIMARY KEY fills itself in if we leave it out.

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL
);

INSERT INTO students (student_id, name) VALUES
    (1, 'Asha'),
    (2, 'Ravi');

INSERT INTO students (name) VALUES ('Meena');

-- REJECTED ON PURPOSE: the id 1 already belongs to Asha.

INSERT INTO students (student_id, name) VALUES (1, 'Copy');

SELECT student_id, name
FROM students
ORDER BY student_id;

-- A surprise in SQLite: a TEXT primary key may hold NULL unless we add NOT NULL.
-- Only INTEGER PRIMARY KEY is always safe.

CREATE TABLE class_codes (
    code  TEXT PRIMARY KEY,
    label TEXT NOT NULL
);

INSERT INTO class_codes (code, label) VALUES (NULL, 'A row with no code');

SELECT code, label
FROM class_codes;