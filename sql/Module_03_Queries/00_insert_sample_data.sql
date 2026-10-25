-- ==========================================
-- Module 03 : Insert Sample Data
-- ==========================================

-- Departments

INSERT INTO departments(dept_id, department_name)
VALUES
(1,'Artificial Intelligence'),
(2,'Human Resources'),
(3,'Finance'),
(4,'Sales'),
(5,'IT');


-- Employees

INSERT INTO employees
(emp_id,name,email,salary,dept_id)
VALUES
(101,'John','john@gmail.com',70000,1),
(102,'Sara','sara@gmail.com',85000,2),
(103,'David','david@gmail.com',65000,3),
(104,'Priya','priya@gmail.com',90000,1),
(105,'Alex','alex@gmail.com',72000,5),
(106,'Maria','maria@gmail.com',78000,4),
(107,'Ahmed','ahmed@gmail.com',68000,1),
(108,'Sophia','sophia@gmail.com',95000,2),
(109,'James','james@gmail.com',61000,3),
(110,'Emma','emma@gmail.com',82000,5);


-- Company Projects

INSERT INTO company_projects
(project_id,project_name,emp_id)
VALUES
(1,'RAG Chatbot',101),
(2,'Recruitment AI',102),
(3,'AI Search Engine',104),
(4,'Payroll System',103),
(5,'Sales Dashboard',106),
(6,'HR Portal',108);