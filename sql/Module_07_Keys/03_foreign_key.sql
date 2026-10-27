-- Lesson 3 of 6 | FOREIGN KEY
-- A FOREIGN KEY is a column that must point to a real row in another table.
-- Example: a student can only be put in a class that exists.
-- The table being pointed to is the parent (classes). The table that points is the child.
-- SQLite checks foreign keys only when PRAGMA foreign_keys is ON.
-- The get_connection function in config.py switches it on. A plain connect does not.
-- ON DELETE CASCADE means: when a parent row is deleted, its child rows are deleted too.

CREATE TABLE classes (
    class_id   INTEGER PRIMARY KEY,
    class_name TEXT NOT NULL
);

CREATE TABLE class_students (
    student_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    class_id   INTEGER NOT NULL,
    FOREIGN KEY (class_id) REFERENCES classes (class_id)
);

CREATE TABLE class_homework (
    homework_id INTEGER PRIMARY KEY,
    title       TEXT NOT NULL,
    class_id    INTEGER NOT NULL,
    FOREIGN KEY (class_id) REFERENCES classes (class_id) ON DELETE CASCADE
);

INSERT INTO classes (class_id, class_name) VALUES
    (1, 'Python Basics'),
    (2, 'SQL Basics'),
    (3, 'Spare class');

INSERT INTO class_students (student_id, name, class_id) VALUES
    (1, 'Asha', 1),
    (2, 'Ravi', 2);

INSERT INTO class_homework (homework_id, title, class_id) VALUES
    (1, 'Variables worksheet', 3),
    (2, 'Loops worksheet',     3),
    (3, 'Joins worksheet',     2);

PRAGMA foreign_keys;

SELECT s.name, c.class_name
FROM class_students AS s
JOIN classes AS c ON c.class_id = s.class_id
ORDER BY s.student_id;

SELECT homework_id, title, class_id
FROM class_homework
ORDER BY homework_id;

-- REJECTED ON PURPOSE: there is no class 99.

INSERT INTO class_students (student_id, name, class_id)
VALUES (3, 'Meena', 99);

-- REJECTED ON PURPOSE: Asha is still in class 1.

DELETE FROM classes
WHERE class_id = 1;

-- Allowed: nobody is in class 3, so it can go. Its homework is deleted with it.

DELETE FROM classes
WHERE class_id = 3;