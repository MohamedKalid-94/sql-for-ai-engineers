# Module 02: SQL Tables

Create, inspect, change and remove tables, and see every constraint refuse bad data.

Run: `python run_module.py 2` | Output: `outputs/Module_02_Table/output.txt` | Starts from: an empty database

## Lessons

| Script | Topic |
|---|---|
| 01 create_tables | `CREATE TABLE`, `INSERT` |
| 02 show_tables | `sqlite_master`, `PRAGMA table_info` |
| 03 rename_table | `ALTER TABLE ... RENAME TO` |
| 04 truncate_table | `DELETE FROM` and resetting `sqlite_sequence` |
| 05 clone_table | `CREATE TABLE ... AS SELECT` (the clone loses its keys) |
| 06 temporary_table | `CREATE TEMP TABLE`, gone when the connection closes |
| 07 alter_table | add, rename and drop a column; changing a column type is not possible |
| 08 constraints | PRIMARY KEY, UNIQUE, NOT NULL, CHECK, DEFAULT, FOREIGN KEY, each rejected on purpose |
| 09 delete_table_data | `DELETE` with and without `WHERE`, undone by rollback |
| 10 drop_tables | `DROP TABLE`, `IF EXISTS` |

## SQLite notes

- There is no `TRUNCATE TABLE`.
- `DROP COLUMN` needs SQLite 3.35.
- Foreign keys are checked only when `PRAGMA foreign_keys` is on. `config.get_connection()` turns it on.