SELECT
employees.emp_name,
departments.department_name

FROM employees

JOIN departments

USING(department_id);