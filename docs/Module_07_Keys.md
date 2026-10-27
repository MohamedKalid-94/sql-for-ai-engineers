# Module 07: SQL Keys

Keys are rules that keep rows identifiable and connected. Every lesson ends by trying to break its rule.

Run: `python run_module.py 7` | Output: `outputs/Module_07_Keys/output.txt` | Starts from: the shared tables

## Lessons

| Script | Topic |
|---|---|
| 01 unique_key | no repeats, but many NULLs are allowed |
| 02 primary_key | `INTEGER PRIMARY KEY`, and a `TEXT` key that accepts NULL |
| 03 foreign_key | rejected inserts and deletes, `ON DELETE CASCADE`, and the foreign key setting |
| 04 composite_key | two columns together as the key |
| 05 alternate_key | other `UNIQUE NOT NULL` columns that could name a row |
| 06 keys_in_real_tables | reading keys back with `PRAGMA table_info`, `index_list`, `foreign_key_list` |

## Key ideas

- SQLite checks foreign keys only when `PRAGMA foreign_keys` is on. Lesson 03 shows a plain connection accepting a student in a class that does not exist.
- Add `NOT NULL` to a `TEXT PRIMARY KEY`, or SQLite allows NULL in it.