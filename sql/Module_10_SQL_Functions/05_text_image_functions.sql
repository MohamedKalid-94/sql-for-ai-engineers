-- Lesson 5 of 11 | Text and Image Functions (SQLite equivalent)
-- SQL Server has TEXT and IMAGE data types. SQLite has TEXT for words and BLOB for raw bytes.
-- A picture, a PDF or any file is just bytes, so it is stored as a BLOB.
-- LENGTH counts characters for TEXT but bytes for a BLOB.
-- HEX shows the bytes. SUBSTR can cut a BLOB by bytes. CAST switches between TEXT and BLOB.
-- The letter e with an accent is made with CHAR(233), so this file stays plain ASCII.
-- The question marks are filled in by Python, which supplies the picture bytes.

SELECT 'h' || CHAR(233) || 'llo'                         AS word,
       LENGTH('h' || CHAR(233) || 'llo')                 AS letters,
       LENGTH(CAST('h' || CHAR(233) || 'llo' AS BLOB))   AS bytes,
       TYPEOF('h' || CHAR(233) || 'llo')                 AS type_of_text,
       TYPEOF(CAST('h' || CHAR(233) || 'llo' AS BLOB))   AS type_of_bytes;

SELECT HEX('Hi')            AS text_as_hex,
       HEX(X'FF00')         AS bytes_as_hex,
       UNICODE('A')         AS code_of_A,
       CHAR(72, 105)        AS text_from_codes,
       LENGTH(ZEROBLOB(8))  AS empty_bytes;

CREATE TABLE stored_files (
    file_id   INTEGER PRIMARY KEY,
    file_name TEXT NOT NULL,
    kind      TEXT NOT NULL,
    content   BLOB NOT NULL
);

INSERT INTO stored_files (file_name, kind, content)
VALUES (?, ?, ?);

SELECT file_name,
       kind,
       TYPEOF(content)                 AS stored_as,
       LENGTH(content)                 AS size,
       HEX(SUBSTR(content, 1, 4))      AS first_four_bytes
FROM stored_files
ORDER BY file_id;

SELECT file_name,
       HEX(SUBSTR(content, 1, 8)) = '89504E470D0A1A0A' AS has_png_signature,
       HEX(SUBSTR(content, 17, 4))                      AS width_field,
       HEX(SUBSTR(content, 21, 4))                      AS height_field
FROM stored_files
WHERE kind = 'image';

SELECT SUM(LENGTH(CAST(content AS BLOB))) AS total_bytes_stored
FROM stored_files;

SELECT content
FROM stored_files
WHERE file_name = ?;