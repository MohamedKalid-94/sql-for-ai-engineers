-- Lesson 9 of 11 | JSON Functions
-- JSON is the text format that web APIs and AI tools use to pass data around.
-- SQLite stores JSON as ordinary text, and has functions that read and build it.
-- json_extract reads a value, using a path such as $.name or $.address.city or $.skills[0].
-- json_each turns a JSON list into rows, one row for each item.
-- json_valid checks that a piece of text really is JSON, so the table can refuse anything else.

CREATE TABLE user_profiles (
    profile_id INTEGER PRIMARY KEY,
    profile    TEXT NOT NULL CHECK (json_valid(profile))
);

INSERT INTO user_profiles (profile) VALUES
    ('{"name":"Asha","age":30,"skills":["SQL","Python","RAG"],"address":{"city":"Pune","country":"India"}}'),
    ('{"name":"Ravi","age":25,"skills":["SQL","HTML"],"address":{"city":"Delhi","country":"India"}}'),
    ('{"name":"Meena","age":28,"skills":["Python","LangGraph","FastAPI","SQL"],"address":{"city":"Chennai","country":"India"}}');

SELECT profile_id,
       json_extract(profile, '$.name')         AS name,
       json_extract(profile, '$.age')          AS age,
       json_extract(profile, '$.address.city') AS city
FROM user_profiles
ORDER BY profile_id;

SELECT json_extract(profile, '$.name')   AS name,
       json_extract(profile, '$.skills[0]') AS first_skill,
       json_array_length(profile, '$.skills') AS skill_count
FROM user_profiles
ORDER BY profile_id;

SELECT json_extract(p.profile, '$.name') AS name,
       s.value                           AS skill
FROM user_profiles AS p, json_each(p.profile, '$.skills') AS s
WHERE s.value = 'Python'
ORDER BY p.profile_id;

SELECT s.value AS skill,
       COUNT(*) AS people
FROM user_profiles AS p, json_each(p.profile, '$.skills') AS s
GROUP BY s.value
ORDER BY people DESC, skill;

SELECT json_object('emp_id', emp_id, 'name', name) AS as_json
FROM employees
ORDER BY emp_id
LIMIT 2;

SELECT json_group_array(name) AS names_in_ai
FROM (SELECT name FROM employees WHERE dept_id = 1 ORDER BY name);

UPDATE user_profiles
SET profile = json_set(profile, '$.age', 31, '$.address.city', 'Mumbai')
WHERE profile_id = 1;

SELECT json_extract(profile, '$.name')         AS name,
       json_extract(profile, '$.age')          AS age,
       json_extract(profile, '$.address.city') AS city,
       profile
FROM user_profiles
WHERE profile_id = 1;

-- The next statement is REJECTED ON PURPOSE.
-- The text is not valid JSON, because the name has no quotes around it.

INSERT INTO user_profiles (profile) VALUES ('{name: Asha}');