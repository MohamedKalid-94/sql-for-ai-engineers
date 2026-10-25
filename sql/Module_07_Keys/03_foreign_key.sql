-- FOREIGN KEY

PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS employees_fk;
DROP TABLE IF EXISTS departments_fk;


CREATE TABLE departments_fk
(
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT
);


CREATE TABLE employees_fk
(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER,

    FOREIGN KEY(dept_id)
    REFERENCES departments_fk(dept_id)
);


INSERT INTO departments_fk VALUES
(1,'AI'),
(2,'Python');


INSERT INTO employees_fk VALUES
(101,'John',1),
(102,'Sara',2);


SELECT
employees_fk.name,
departments_fk.dept_name

FROM employees_fk

JOIN departments_fk

ON employees_fk.dept_id =
departments_fk.dept_id;