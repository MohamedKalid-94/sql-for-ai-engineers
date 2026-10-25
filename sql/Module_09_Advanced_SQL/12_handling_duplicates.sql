-- Handling Duplicates

DROP TABLE IF EXISTS duplicate_employees;

CREATE TABLE duplicate_employees(
    emp_id INTEGER,
    name TEXT
);

INSERT INTO duplicate_employees VALUES
(101,'John'),
(101,'John'),
(102,'Sara'),
(102,'Sara'),
(103,'David');

SELECT * FROM duplicate_employees;

SELECT DISTINCT *
FROM duplicate_employees;