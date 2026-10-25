-- DATE Functions

SELECT DATE('now') AS current_date;

SELECT TIME('now') AS current_time;

SELECT DATETIME('now') AS current_datetime;

SELECT emp_name,
       joining_date,
       DATE(joining_date,'+30 days') AS probation_end
FROM employees;

SELECT STRFTIME('%Y', joining_date) AS joining_year
FROM employees;

SELECT JULIANDAY('now') - JULIANDAY(joining_date) AS days_since_joining
FROM employees
WHERE joining_date IS NOT NULL;