-- DEFAULT Constraint

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    status TEXT DEFAULT 'Active'
);

INSERT INTO users(user_id,username)
VALUES
(1,'Kalid');

SELECT * FROM users;