-- Lesson 3 of 10 | Rename Table
-- ALTER TABLE ... RENAME TO writes a new title on the page.
-- The rows inside stay exactly as they were.

CREATE TABLE projects (
    project_id   INTEGER PRIMARY KEY,
    project_name TEXT NOT NULL
);

INSERT INTO projects (project_name) VALUES ('RAG chatbot'), ('SQL portfolio');

SELECT name
FROM sqlite_master
WHERE type = 'table'
  AND name NOT LIKE 'sqlite_%'
ORDER BY name;

ALTER TABLE projects RENAME TO company_projects;

SELECT project_id, project_name
FROM company_projects
ORDER BY project_id;