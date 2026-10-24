-- ===========================================
-- Module 02 - Create Tables
-- ===========================================

CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    salary REAL CHECK(salary >= 0),
    dept_id INTEGER,
    FOREIGN KEY(dept_id)
        REFERENCES departments(dept_id)
);

CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL,
    emp_id INTEGER,
    FOREIGN KEY(emp_id)
        REFERENCES employees(emp_id)
);