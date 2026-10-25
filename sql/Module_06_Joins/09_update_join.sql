-- UPDATE JOIN Equivalent


UPDATE employees

SET salary = salary + 5000


WHERE department_id IN

(
    SELECT department_id
    FROM departments
    WHERE department_name='AI'
);



SELECT *
FROM employees;