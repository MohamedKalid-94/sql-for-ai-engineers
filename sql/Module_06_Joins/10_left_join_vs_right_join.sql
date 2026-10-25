-- LEFT JOIN

SELECT

employees.emp_name,
departments.department_name


FROM employees


LEFT JOIN departments


ON employees.department_id =
departments.department_id;



-- RIGHT JOIN Equivalent

SELECT

departments.department_name,
employees.emp_name


FROM departments


LEFT JOIN employees


ON departments.department_id =
employees.department_id;