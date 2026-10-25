-- ==========================================
-- Module 04 : Create View
-- ==========================================

CREATE VIEW employee_details AS

SELECT
    e.emp_id,
    e.name,
    e.email,
    e.salary,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;