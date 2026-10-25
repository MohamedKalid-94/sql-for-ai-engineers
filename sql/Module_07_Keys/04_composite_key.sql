-- COMPOSITE KEY


DROP TABLE IF EXISTS employee_projects;


CREATE TABLE employee_projects
(
    emp_id INTEGER,
    project_id INTEGER,

    PRIMARY KEY(emp_id,project_id)
);


INSERT INTO employee_projects
VALUES
(101,1);


INSERT INTO employee_projects
VALUES
(101,2);


INSERT INTO employee_projects
VALUES
(102,1);



SELECT *
FROM employee_projects;