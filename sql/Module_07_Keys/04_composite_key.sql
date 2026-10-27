-- Lesson 4 of 6 | COMPOSITE KEY
-- A composite key uses TWO or more columns together to identify a row.
-- Example: a student can join many classes, and a class has many students,
-- but the same student cannot join the same class twice.
-- So neither student_id nor class_id is unique alone, but the PAIR is.

CREATE TABLE enrollments (
    student_id  INTEGER NOT NULL,
    class_id    INTEGER NOT NULL,
    enrolled_on TEXT NOT NULL,
    PRIMARY KEY (student_id, class_id)
);

INSERT INTO enrollments (student_id, class_id, enrolled_on) VALUES
    (1, 1, '2025-06-01'),
    (1, 2, '2025-06-02'),
    (2, 1, '2025-06-01');

SELECT student_id, class_id, enrolled_on
FROM enrollments
ORDER BY student_id, class_id;

-- REJECTED ON PURPOSE: student 1 is already in class 1.

INSERT INTO enrollments (student_id, class_id, enrolled_on)
VALUES (1, 1, '2025-06-10');