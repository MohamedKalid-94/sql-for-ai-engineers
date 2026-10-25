-- UNION combines rows

SELECT emp_name
FROM employees

UNION

SELECT department_name
FROM departments;



-- JOIN combines columns

SELECT

employees.emp_name,
departments.department_name


FROM employees


JOIN departments


ON employees.department_id =
departments.department_id;