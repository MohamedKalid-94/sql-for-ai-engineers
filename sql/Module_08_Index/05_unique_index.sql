-- Lesson 5 of 7 | Unique Index
-- A UNIQUE index is an index with a rule attached: no two rows may hold the same value.
-- It is both a fast lookup and a guard. Think of roll codes, where no two pupils share one.
-- CREATE UNIQUE INDEX works on a column that already has data, but only if that data has no repeats.

CREATE UNIQUE INDEX idx_pupils_roll_code ON pupils (roll_code);

EXPLAIN QUERY PLAN
SELECT pupil_id, name
FROM pupils
WHERE roll_code = 'R00123';

SELECT pupil_id, name
FROM pupils
WHERE roll_code = 'R00123';

-- The next statement is REJECTED ON PURPOSE.
-- The roll code R00001 already belongs to pupil 1.

INSERT INTO pupils (pupil_id, name, city, marks, roll_code)
VALUES (20001, 'Copycat', 'Pune', 50, 'R00001');

-- The next statement is REJECTED ON PURPOSE.
-- Many pupils share a city, so city cannot be unique.

CREATE UNIQUE INDEX idx_pupils_city_unique ON pupils (city);

SELECT COUNT(*) AS pupils_in_table
FROM pupils;