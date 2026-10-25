-- Date & Time

SELECT DATE('now');

SELECT TIME('now');

SELECT DATETIME('now');

SELECT *
FROM employees
WHERE joining_date IS NOT NULL;