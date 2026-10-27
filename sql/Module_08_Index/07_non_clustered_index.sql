-- Lesson 7 of 7 | Non-Clustered Index
-- A non-clustered index is a separate sorted list that points back to the rows of the table.
-- Every ordinary CREATE INDEX in SQLite is non-clustered, and a table can have many of them.
-- An index on two columns (city, marks) helps when a query uses city first, or city and marks together.
-- A covering index holds every column the query needs, so SQLite never has to visit the table at all.

CREATE INDEX idx_pupils_city_marks ON pupils (city, marks);

EXPLAIN QUERY PLAN
SELECT pupil_id, name
FROM pupils
WHERE city = 'Pune' AND marks = 77;

EXPLAIN QUERY PLAN
SELECT city, marks
FROM pupils
WHERE city = 'Pune' AND marks = 77;

SELECT COUNT(*) AS pune_pupils_with_77_marks
FROM pupils
WHERE city = 'Pune' AND marks = 77;

SELECT name AS index_name, "unique" AS is_unique, origin
FROM pragma_index_list('pupils')
ORDER BY name;