-- Column Alias

SELECT
name AS employee_name,
salary AS monthly_salary
FROM employees;



-- Table Alias

SELECT
e.name,
e.salary
FROM employees AS e;