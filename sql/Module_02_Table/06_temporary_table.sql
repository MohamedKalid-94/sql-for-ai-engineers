-- ============================================
-- Module 02
-- Temporary Table
-- ============================================

CREATE TEMP TABLE temp_employee_salary AS

SELECT
    emp_id,
    name,
    salary
FROM employees;