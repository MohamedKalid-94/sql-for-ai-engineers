-- Create Index

CREATE INDEX idx_employee_salary
ON employees(salary);


-- Verify using query

SELECT *
FROM employees
WHERE salary > 80000;