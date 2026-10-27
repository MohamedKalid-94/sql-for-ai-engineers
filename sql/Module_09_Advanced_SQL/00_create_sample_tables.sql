-- Lesson 0 of 20 | Create Sample Tables
-- The shared setup gave this module 5 employees and 5 departments.
-- Several lessons need missing values (NULL), so David and Alex lose their joining date.
-- Sara, David and Alex already have no phone number.

UPDATE employees
SET joining_date = NULL
WHERE emp_id IN (103, 105);

SELECT emp_id, name, phone, joining_date
FROM employees
ORDER BY emp_id;