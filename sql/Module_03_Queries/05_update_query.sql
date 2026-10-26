-- Lesson 5 of 7 | UPDATE
-- UPDATE changes existing rows. The WHERE part decides WHICH rows change.
-- Forget WHERE and EVERY row changes, so check the row count and keep a rollback ready.

SELECT emp_id, name, salary
FROM employees
WHERE emp_id IN (101, 103, 108)
ORDER BY emp_id;

UPDATE employees
SET salary = 80000
WHERE emp_id = 101;

UPDATE employees
SET salary = ROUND(salary * 1.10, 2)
WHERE dept_id = 3;

UPDATE employees
SET phone = '9111111111',
    joining_date = '2025-05-01'
WHERE emp_id = 108;

SELECT emp_id, name, salary, phone, joining_date
FROM employees
WHERE emp_id IN (101, 103, 108)
ORDER BY emp_id;

-- DANGER: no WHERE, so every employee is changed

UPDATE employees
SET is_active = 0;

SELECT COUNT(*) AS inactive_employees
FROM employees
WHERE is_active = 0;