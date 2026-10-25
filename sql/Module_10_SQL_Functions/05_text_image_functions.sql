-- TEXT & BLOB Functions

DROP TABLE IF EXISTS files;

CREATE TABLE files
(
    id INTEGER PRIMARY KEY,
    file_name TEXT,
    file_data BLOB
);

INSERT INTO files(file_name,file_data)
VALUES
('sample.txt',X'48656C6C6F');

SELECT
file_name,
LENGTH(file_data) AS blob_size
FROM files;

SELECT
LENGTH(file_name)
FROM files;