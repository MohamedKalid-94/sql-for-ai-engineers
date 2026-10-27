-- Lesson 7 of 20 | DEFAULT Constraint
-- DEFAULT is the value SQLite fills in when we leave a column out of an INSERT.
-- A default can be a plain value, or an expression written in brackets.
-- The expression below uses a fixed date, so the result is the same on every run.
-- Careful: DEFAULT is used only when the column is left out. Writing NULL on purpose does not trigger it.

CREATE TABLE tickets (
    ticket_id INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    status    TEXT NOT NULL DEFAULT 'Open',
    priority  INTEGER NOT NULL DEFAULT 3,
    due_on    TEXT NOT NULL DEFAULT (date('2025-01-01', '+7 days'))
);

INSERT INTO tickets (title)
VALUES ('Fix login page'), ('Update README');

INSERT INTO tickets (title, status, priority)
VALUES ('Server down', 'Urgent', 1);

-- The next statement is REJECTED ON PURPOSE.
-- Writing NULL is not the same as leaving the column out.

INSERT INTO tickets (title, status)
VALUES ('Bad ticket', NULL);

SELECT ticket_id, title, status, priority, due_on
FROM tickets
ORDER BY ticket_id;

SELECT name, dflt_value
FROM pragma_table_info('tickets')
WHERE dflt_value IS NOT NULL
ORDER BY cid;