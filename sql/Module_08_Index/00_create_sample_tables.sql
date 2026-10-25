-- ==========================================================
-- Module 08: SQL Indexes
-- File: 00_create_sample_tables.sql
-- Purpose: Create sample tables for Index examples
-- ==========================================================


-- Drop existing table
DROP TABLE IF EXISTS employees;


-- Create Employees Table

CREATE TABLE employees
(
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    email TEXT,
    salary REAL,
    department_id INTEGER
);


-- Insert Sample Data

INSERT INTO employees
(emp_id, emp_name, email, salary, department_id)
VALUES

(101, 'John', 'john@gmail.com', 75000, 1),

(102, 'Sara', 'sara@gmail.com', 85000, 2),

(103, 'David', 'david@gmail.com', 65000, 3),

(104, 'Priya', 'priya@gmail.com', 90000, 1),

(105, 'Alex', 'alex@gmail.com', 72000, 5);


-- Verify Data

SELECT *
FROM employees;