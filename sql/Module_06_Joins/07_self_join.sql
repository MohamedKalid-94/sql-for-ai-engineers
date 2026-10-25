-- SELF JOIN
-- Employee and Manager Relationship


SELECT

employee.emp_name AS Employee,

manager.emp_name AS Manager


FROM employees employee


LEFT JOIN employees manager


ON employee.manager_id =
manager.emp_id;