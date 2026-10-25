-- Module 05: SQL Operators and Clauses
-- Topic: IS NOT NULL Operator

-- Update sample joining dates
UPDATE employees
SET joining_date = '2026-01-01'
WHERE emp_id IN (101,102,103);


-- Select employees having joining date
SELECT *
FROM employees
WHERE joining_date IS NOT NULL;