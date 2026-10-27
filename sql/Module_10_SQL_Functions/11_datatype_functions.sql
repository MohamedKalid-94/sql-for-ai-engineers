-- Lesson 11 of 11 | Datatype Functions
-- Every SQLite value has one of five storage classes: NULL, INTEGER, REAL, TEXT or BLOB.
-- TYPEOF tells us which one a value has right now.
-- A column's declared type, such as INTEGER, is only a preference called affinity and not a strict rule.
-- SQLite tries to convert a value to the declared type, but keeps it as it is when it cannot.
-- A STRICT table (SQLite 3.37 or newer) makes the declared type a real rule.

SELECT TYPEOF(42)       AS a_whole_number,
       TYPEOF(3.14)     AS a_decimal,
       TYPEOF('hello')  AS some_text,
       TYPEOF(X'FF')    AS raw_bytes,
       TYPEOF(NULL)     AS no_value;

SELECT TYPEOF(1 + 1)     AS integer_plus_integer,
       TYPEOF(1 + 1.0)   AS integer_plus_real,
       TYPEOF(7 / 2)     AS integer_division,
       TYPEOF('5' + 1)   AS text_plus_number,
       TYPEOF('5' || 1)  AS text_joined;

CREATE TABLE flexible (
    id     INTEGER PRIMARY KEY,
    amount INTEGER,
    label  TEXT
);

INSERT INTO flexible (amount, label) VALUES
    (10,    'ten'),
    ('20',  'twenty'),
    (30.0,  'thirty'),
    (30.5,  'thirty and a half'),
    ('abc', 'letters'),
    (NULL,  'nothing'),
    (5,     99);

SELECT id,
       amount,
       TYPEOF(amount) AS amount_stored_as,
       label,
       TYPEOF(label)  AS label_stored_as
FROM flexible
ORDER BY id;

SELECT name AS column_name, type AS declared_type
FROM pragma_table_info('flexible')
ORDER BY cid;

CREATE TABLE strict_amounts (
    id     INTEGER PRIMARY KEY,
    amount INTEGER NOT NULL,
    label  TEXT NOT NULL
) STRICT;

INSERT INTO strict_amounts (amount, label) VALUES
    (10,   'ten'),
    ('20', 'twenty');

-- The next statement is REJECTED ON PURPOSE.
-- A STRICT table refuses text that cannot become a whole number.

INSERT INTO strict_amounts (amount, label)
VALUES ('abc', 'letters');

SELECT id, amount, TYPEOF(amount) AS amount_stored_as
FROM strict_amounts
ORDER BY id;