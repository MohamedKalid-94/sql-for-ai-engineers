# Module 04: SQL Views

A view is a saved question. It stores the query, not the data, so it always shows the latest rows.

Run: `python run_module.py 4` | Output: `outputs/Module_04_Views/output.txt` | Starts from: the shared tables

## Lessons

| Script | Topic |
|---|---|
| 01 create_views | a filtering view, a joining view, and a view following a table change |
| 02 update_views | views are read-only; changing a view means `DROP VIEW` then `CREATE VIEW` |
| 03 rename_views | create the new name, drop the old one |
| 04 drop_views | `DROP VIEW`, `IF EXISTS`, and the table stays untouched |

## SQLite notes

- No `ALTER VIEW` and no `CREATE OR REPLACE VIEW` (both are shown being rejected).
- You cannot `UPDATE` through a view.