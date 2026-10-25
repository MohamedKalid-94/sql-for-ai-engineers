-- ==========================================
-- Module 04 : Rename View (SQLite Equivalent)
-- ==========================================

DROP VIEW IF EXISTS employee_information;

CREATE VIEW employee_information AS

SELECT
    emp_id,
    name,
    salary
FROM employees;