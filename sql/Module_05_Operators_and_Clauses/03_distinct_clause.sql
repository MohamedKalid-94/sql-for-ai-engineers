-- Lesson 3 of 24 | DISTINCT Clause
-- DISTINCT removes repeated values, so each value shows once.

SELECT dept_id
FROM employees
ORDER BY dept_id;

SELECT DISTINCT dept_id
FROM employees
ORDER BY dept_id;

SELECT COUNT(DISTINCT dept_id) AS departments_with_staff
FROM employees;