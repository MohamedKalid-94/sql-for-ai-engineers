-- NOT NULL Constraint Example

CREATE TABLE employee_test
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
);


INSERT INTO employee_test
(id,name,email)
VALUES
(1,'John','john@gmail.com');


-- This will fail because name cannot be NULL

INSERT INTO employee_test
(id,name,email)
VALUES
(2,NULL,'test@gmail.com');