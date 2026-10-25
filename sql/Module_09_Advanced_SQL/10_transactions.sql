-- Transactions

BEGIN TRANSACTION;

UPDATE employees
SET salary = salary + 5000
WHERE department_id = 1;

COMMIT;

SELECT *
FROM employees;