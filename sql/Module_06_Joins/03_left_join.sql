SELECT
employees.emp_name,
departments.department_name

FROM employees

LEFT JOIN departments

ON employees.department_id =
departments.department_id;