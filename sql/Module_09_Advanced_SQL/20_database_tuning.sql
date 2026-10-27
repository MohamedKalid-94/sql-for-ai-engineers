-- Lesson 20 of 20 | Database Tuning
-- Tuning means helping SQLite answer faster. EXPLAIN QUERY PLAN shows how it plans to answer.
-- SCAN means read every row. SEARCH means jump straight to the matching rows using an index.
-- Tip 1: index the columns you filter on.
-- Tip 2: do not wrap an indexed column in a calculation, because SQLite then cannot use the index.
-- Tip 3: a covering index holds every column the query needs, so the table is never visited.

EXPLAIN QUERY PLAN
SELECT name
FROM employees
WHERE salary > 80000;

CREATE INDEX idx_employees_salary ON employees (salary);

EXPLAIN QUERY PLAN
SELECT name
FROM employees
WHERE salary > 80000;

EXPLAIN QUERY PLAN
SELECT name
FROM employees
WHERE salary + 0 > 80000;

CREATE INDEX idx_employees_dept_salary ON employees (dept_id, salary);

EXPLAIN QUERY PLAN
SELECT dept_id, salary
FROM employees
WHERE dept_id = 1;