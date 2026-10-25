-- String Functions

SELECT UPPER(emp_name)
FROM employees;

SELECT LOWER(emp_name)
FROM employees;

SELECT LENGTH(emp_name)
FROM employees;

SELECT SUBSTR(emp_name,1,3)
FROM employees;

SELECT REPLACE(email,'gmail','company')
FROM employees;

SELECT TRIM('   SQL Functions   ');

SELECT INSTR(email,'@')
FROM employees;