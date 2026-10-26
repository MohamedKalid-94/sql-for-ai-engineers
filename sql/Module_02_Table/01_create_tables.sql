-- Lesson 1 of 10 | Create Table
-- A table is one page of the notebook. Columns are the headings and rows are the lines.
-- We make two tables. departments is the small one.
-- employees points to it through dept_id.

CREATE TABLE departments (
    dept_id   INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
);

CREATE TABLE employees (
    emp_id  INTEGER PRIMARY KEY,
    name    TEXT NOT NULL,
    email   TEXT,
    salary  REAL,
    dept_id INTEGER REFERENCES departments (dept_id)
);

INSERT INTO departments (dept_id, dept_name) VALUES
    (1, 'AI'),
    (2, 'Python'),
    (3, 'Data Science'),
    (4, 'Cloud'),
    (5, 'GenAI');

INSERT INTO employees (emp_id, name, email, salary, dept_id) VALUES
    (101, 'John',  'john@gmail.com',  75000, 1),
    (102, 'Sara',  'sara@gmail.com',  85000, 2),
    (103, 'David', 'david@gmail.com', 65000, 3),
    (104, 'Priya', 'priya@gmail.com', 90000, 1),
    (105, 'Alex',  'alex@gmail.com',  72000, 5);

SELECT dept_id, dept_name
FROM departments
ORDER BY dept_id;

SELECT emp_id, name, email, salary, dept_id
FROM employees
ORDER BY emp_id;