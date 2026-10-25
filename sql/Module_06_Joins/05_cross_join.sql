-- CROSS JOIN
-- Returns Cartesian Product

SELECT
    employees.emp_name,
    departments.department_name

FROM employees

CROSS JOIN departments;