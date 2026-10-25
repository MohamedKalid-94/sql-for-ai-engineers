-- ALTERNATE KEY


DROP TABLE IF EXISTS users;


CREATE TABLE users
(
    user_id INTEGER PRIMARY KEY,

    username TEXT UNIQUE,

    email TEXT UNIQUE
);


INSERT INTO users
VALUES
(
1,
'kalid',
'kalid@gmail.com'
);


INSERT INTO users
VALUES
(
2,
'john',
'john@gmail.com'
);


SELECT *
FROM users;