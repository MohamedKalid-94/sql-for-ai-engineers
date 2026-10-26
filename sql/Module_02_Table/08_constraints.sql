-- Lesson 8 of 10 | Constraints
-- Constraints are the rules of the register. The database enforces them for us.
-- PRIMARY KEY: every row has its own id. UNIQUE: no two rows share this value.
-- NOT NULL: the value cannot be empty. CHECK: the value must pass a test.
-- DEFAULT: the value used when we give none. FOREIGN KEY: must point to a real row elsewhere.

CREATE TABLE employee_constraints (
    emp_id  INTEGER PRIMARY KEY,
    code    TEXT NOT NULL UNIQUE,
    name    TEXT NOT NULL,
    salary  REAL CHECK (salary >= 0),
    status  TEXT DEFAULT 'Active',
    dept_id INTEGER REFERENCES departments (dept_id)
);

INSERT INTO employee_constraints (emp_id, code, name, salary, dept_id)
VALUES (1, 'EMP001', 'John', 70000, 1);

SELECT emp_id, code, name, salary, status, dept_id
FROM employee_constraints;

-- The five statements below are REJECTED ON PURPOSE.
-- Each one breaks exactly one rule.

INSERT INTO employee_constraints (emp_id, code, name, salary, dept_id)
VALUES (1, 'EMP002', 'Sara', 85000, 2);

INSERT INTO employee_constraints (emp_id, code, name, salary, dept_id)
VALUES (2, 'EMP001', 'Sara', 85000, 2);

INSERT INTO employee_constraints (emp_id, code, name, salary, dept_id)
VALUES (3, 'EMP003', NULL, 65000, 3);

INSERT INTO employee_constraints (emp_id, code, name, salary, dept_id)
VALUES (4, 'EMP004', 'Priya', -5, 1);

INSERT INTO employee_constraints (emp_id, code, name, salary, dept_id)
VALUES (5, 'EMP005', 'Alex', 72000, 99);