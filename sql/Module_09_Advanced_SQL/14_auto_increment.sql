-- AUTO INCREMENT

DROP TABLE IF EXISTS auto_increment_demo;

CREATE TABLE auto_increment_demo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT
);

INSERT INTO auto_increment_demo(employee_name)
VALUES
('Alex'),
('Maria'),
('Emma');

SELECT *
FROM auto_increment_demo;