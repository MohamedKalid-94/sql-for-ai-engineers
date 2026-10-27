-- Lesson 0 of 11 | Create Sample Tables
-- The shared setup gave this module 5 employees and 5 departments.
-- Several lessons need numbers to measure, so we add a small table of exam scores.
-- Four pupils each sat three subjects, which makes 12 scores.

CREATE TABLE exam_scores (
    score_id INTEGER PRIMARY KEY,
    student  TEXT NOT NULL,
    subject  TEXT NOT NULL,
    score    INTEGER NOT NULL CHECK (score BETWEEN 0 AND 100)
);

INSERT INTO exam_scores (student, subject, score) VALUES
    ('Asha',  'Maths',   92),
    ('Asha',  'Science', 88),
    ('Asha',  'English', 79),
    ('Ravi',  'Maths',   65),
    ('Ravi',  'Science', 70),
    ('Ravi',  'English', 58),
    ('Meena', 'Maths',   85),
    ('Meena', 'Science', 91),
    ('Meena', 'English', 94),
    ('Kiran', 'Maths',   45),
    ('Kiran', 'Science', 52),
    ('Kiran', 'English', 61);

SELECT COUNT(*) AS scores_in_table
FROM exam_scores;

SELECT student, subject, score
FROM exam_scores
ORDER BY score_id
LIMIT 4;