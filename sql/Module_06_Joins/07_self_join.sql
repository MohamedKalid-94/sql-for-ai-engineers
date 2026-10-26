-- Lesson 7 of 11 | SELF JOIN
-- A SELF JOIN joins a table to itself. We give the table two nicknames,
-- as if it were two copies: e for the employee and m for the manager.
-- manager_id on an employee row holds the emp_id of that employee's manager.
-- John has no manager, so LEFT JOIN is needed to keep him in the list.

SELECT e.name AS employee, m.name AS manager
FROM employees AS e
LEFT JOIN employees AS m ON m.emp_id = e.manager_id
ORDER BY e.emp_id;

SELECT e.name AS employee
FROM employees AS e
JOIN employees AS m ON m.emp_id = e.manager_id
WHERE m.name = 'John'
ORDER BY e.emp_id;

SELECT m.name AS manager, COUNT(*) AS direct_reports
FROM employees AS e
JOIN employees AS m ON m.emp_id = e.manager_id
GROUP BY m.emp_id
ORDER BY direct_reports DESC, manager;