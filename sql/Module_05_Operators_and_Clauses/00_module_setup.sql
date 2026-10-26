-- Lesson 0 of 24 | Module Setup
-- The shared setup gave this module 5 employees and 5 departments.
-- Module 5 needs a little extra data for its demos.
-- David has no joining date (for the NULL lessons) and Alex is inactive (for the true/false lesson).
-- A contractors table gives us a second list of people (for UNION, INTERSECT and EXCEPT).

UPDATE employees SET joining_date = NULL WHERE emp_id = 103;

UPDATE employees SET is_active = 0 WHERE emp_id = 105;

CREATE TABLE contractors (
    contractor_id INTEGER PRIMARY KEY,
    name          TEXT NOT NULL,
    email         TEXT,
    dept_id       INTEGER REFERENCES departments (dept_id)
);

INSERT INTO contractors (contractor_id, name, email, dept_id) VALUES
    (1, 'Maria', 'maria@gmail.com', 1),
    (2, 'Sara',  'sara@gmail.com',  2),
    (3, 'Kumar', 'kumar@gmail.com', 4);

SELECT emp_id, name, joining_date, is_active
FROM employees
ORDER BY emp_id;

SELECT contractor_id, name, dept_id
FROM contractors
ORDER BY contractor_id;