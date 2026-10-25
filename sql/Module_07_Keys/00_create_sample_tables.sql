-- Create Base Tables

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;


CREATE TABLE departments
(
    dept_id INTEGER,
    dept_name TEXT
);


CREATE TABLE employees
(
    emp_id INTEGER,
    name TEXT,
    email TEXT,
    salary REAL,
    dept_id INTEGER
);


INSERT INTO departments VALUES
(1,'AI'),
(2,'Python'),
(3,'Data Science');


INSERT INTO employees VALUES
(101,'John','john@gmail.com',75000,1),
(102,'Sara','sara@gmail.com',85000,2),
(103,'David','david@gmail.com',65000,3);


SELECT * FROM employees;