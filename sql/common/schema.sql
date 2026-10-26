CREATE TABLE departments (
    dept_id   INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL UNIQUE
);

CREATE TABLE employees (
    emp_id       INTEGER PRIMARY KEY,
    name         TEXT    NOT NULL,
    email        TEXT    NOT NULL UNIQUE,
    salary       REAL    NOT NULL CHECK (salary >= 0),
    dept_id      INTEGER REFERENCES departments (dept_id),
    manager_id   INTEGER REFERENCES employees (emp_id),
    phone        TEXT,
    joining_date TEXT,
    is_active    INTEGER NOT NULL DEFAULT 1
);