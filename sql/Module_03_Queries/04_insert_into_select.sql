-- Lesson 4 of 7 | INSERT INTO SELECT
-- Copy rows from one table into an existing table in a single command.
-- RULE: name the columns on BOTH sides, in the same order and the same count.
-- Without names, INSERT ... SELECT * fails when the two tables have different columns.

CREATE TABLE employees_backup (
    emp_id  INTEGER PRIMARY KEY,
    name    TEXT NOT NULL,
    email   TEXT,
    salary  REAL,
    dept_id INTEGER
);

INSERT INTO employees_backup (emp_id, name, email, salary, dept_id)
SELECT emp_id, name, email, salary, dept_id
FROM employees
WHERE dept_id = 1;

SELECT emp_id, name, salary, dept_id
FROM employees_backup
ORDER BY emp_id;

-- The next statement is REJECTED ON PURPOSE.
-- employees has 9 columns but employees_backup has 5, so SELECT * does not fit.

INSERT INTO employees_backup
SELECT * FROM employees;