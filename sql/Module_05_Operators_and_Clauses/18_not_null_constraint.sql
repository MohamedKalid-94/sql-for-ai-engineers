-- Lesson 18 of 24 | NOT NULL Constraint
-- NOT NULL is a rule on a column: the value can never be left empty.
-- The database enforces the rule, so bad data never gets in.

CREATE TABLE trainees (
    trainee_id INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    city       TEXT
);

INSERT INTO trainees (name, email, city)
VALUES ('Maya', 'maya@gmail.com', 'Pune');

-- The next statement is REJECTED ON PURPOSE.
-- It leaves the name empty, which the NOT NULL rule does not allow.

INSERT INTO trainees (name, email, city)
VALUES (NULL, 'ghost@gmail.com', 'Chennai');

SELECT trainee_id, name, email, city
FROM trainees;