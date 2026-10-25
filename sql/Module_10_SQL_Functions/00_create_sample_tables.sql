-- =====================================================
-- Module 10 : SQL Functions
-- 00_create_sample_tables.sql
-- =====================================================

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    email TEXT UNIQUE,
    salary REAL,
    department_id INTEGER,
    phone TEXT,
    joining_date DATE,
    is_active INTEGER
);

INSERT INTO employees
(emp_id, emp_name, email, salary, department_id, phone, joining_date, is_active)
VALUES
(101,'John','john@gmail.com',75000,1,'9876543210','2025-01-15',1),
(102,'Sara','sara@gmail.com',85000,2,NULL,'2025-02-10',1),
(103,'David','david@gmail.com',65000,3,NULL,NULL,1),
(104,'Priya','priya@gmail.com',90000,1,'9123456780','2024-12-01',1),
(105,'Alex','alex@gmail.com',72000,5,NULL,NULL,1);