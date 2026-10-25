-- Clustered Index Concept

-- SQLite does not support explicit clustered indexes.
-- Primary Key internally uses row storage optimization.

CREATE TABLE employee_clustered
(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
);


INSERT INTO employee_clustered VALUES
(101,'John',75000),
(102,'Sara',85000),
(103,'David',65000);


SELECT *
FROM employee_clustered;