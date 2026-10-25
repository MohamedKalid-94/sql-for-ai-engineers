-- UNIQUE KEY

DROP TABLE IF EXISTS employees_unique;


CREATE TABLE employees_unique
(
    emp_id INTEGER,
    email TEXT UNIQUE
);


INSERT INTO employees_unique
VALUES
(101,'john@gmail.com');


INSERT INTO employees_unique
VALUES
(102,'sara@gmail.com');


SELECT *
FROM employees_unique;