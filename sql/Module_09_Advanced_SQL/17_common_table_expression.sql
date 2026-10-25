-- Common Table Expression (CTE)

WITH HighSalaryEmployees AS
(
    SELECT *
    FROM employees
    WHERE salary > 75000
)

SELECT *
FROM HighSalaryEmployees;