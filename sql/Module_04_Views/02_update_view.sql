-- ==========================================
-- Module 04 : Update View (SQLite Equivalent)
-- ==========================================

DROP VIEW IF EXISTS employee_details;

CREATE VIEW employee_details AS

SELECT
    emp_id,
    name,
    salary
FROM employees;