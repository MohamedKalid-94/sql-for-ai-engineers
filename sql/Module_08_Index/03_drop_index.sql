-- Drop Index

DROP INDEX idx_employee_salary;


-- Verify after deleting index

SELECT *
FROM employees
WHERE salary > 80000;