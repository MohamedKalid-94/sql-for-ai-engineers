-- PRIMARY KEY

DROP TABLE IF EXISTS employees_primary;


CREATE TABLE employees_primary
(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
);


INSERT INTO employees_primary
VALUES
(101,'John',75000);


INSERT INTO employees_primary
VALUES
(102,'Sara',85000);


SELECT *
FROM employees_primary;