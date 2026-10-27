-- Lesson 5 of 20 | NULL Functions
-- COALESCE gives the first value that is not NULL, so it fills blanks. It can take many values.
-- IFNULL is the two-value version of COALESCE.
-- NULLIF gives NULL when its two values are equal, and the first value otherwise.
-- IIF is a short if / else: IIF(test, value_if_true, value_if_false).

SELECT name, COALESCE(phone, 'Not available') AS phone
FROM employees
ORDER BY emp_id;

SELECT name, IFNULL(joining_date, 'Not joined') AS joining_date
FROM employees
ORDER BY emp_id;

SELECT name, COALESCE(phone, email, 'no contact') AS best_contact
FROM employees
ORDER BY emp_id;

SELECT NULLIF(10, 10) AS same_values,
       NULLIF(10, 20) AS different_values;

SELECT AVG(salary)              AS plain_average,
       AVG(NULLIF(salary, 65000)) AS average_without_65000
FROM employees;

SELECT name, IIF(phone IS NULL, 'No phone', 'Has phone') AS phone_status
FROM employees
ORDER BY emp_id;