-- Using Sequences

-- SQLite does not support SEQUENCE objects.
-- INTEGER PRIMARY KEY behaves like a sequence.

DROP TABLE IF EXISTS sequence_demo;

CREATE TABLE sequence_demo(
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO sequence_demo(name)
VALUES
('John'),
('Sara'),
('David');

SELECT * FROM sequence_demo;