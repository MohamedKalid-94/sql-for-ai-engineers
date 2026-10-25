-- Non Clustered Index

CREATE INDEX idx_employee_department
ON employees(department_id);


SELECT *
FROM employees
WHERE department_id = 1;