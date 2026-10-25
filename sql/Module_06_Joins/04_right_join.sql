-- RIGHT JOIN Equivalent in SQLite

SELECT
    departments.department_name,
    employees.emp_name

FROM departments

LEFT JOIN employees

ON departments.department_id =
employees.department_id;