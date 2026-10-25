SELECT
employees.emp_name,
employees.salary,
departments.department_name

FROM employees

INNER JOIN departments

ON employees.department_id =
departments.department_id;