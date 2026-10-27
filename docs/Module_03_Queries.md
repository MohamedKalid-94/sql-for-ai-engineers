# Module 03: SQL Queries

Add, read, change and remove rows.

Run: `python run_module.py 3` | Output: `outputs/Module_03_Queries/output.txt` | Starts from: the shared `employees` and `departments` tables

## Lessons

| Script | Topic |
|---|---|
| 00 insert_sample_data | two more employees, with named columns |
| 01 insert_query | one row, many rows, and `?` placeholders |
| 02 select_query | columns, `WHERE`, calculated columns, `COUNT`, `MAX`, `MIN` |
| 03 select_into | `CREATE TABLE ... AS SELECT` |
| 04 insert_into_select | copying rows with named columns, and the error `SELECT *` causes |
| 05 update_query | `UPDATE ... WHERE`, then the no-`WHERE` danger undone by rollback |
| 06 delete_query | preview with `SELECT`, delete, rollback |
| 07 sorting_results | `ASC`, `DESC`, tie-breakers, `LIMIT` |

## Key ideas

- Always name the columns in `INSERT` and `INSERT ... SELECT`.
- Run a `SELECT` with the same `WHERE` before an `UPDATE` or `DELETE`.
- `SELECT ... INTO` is SQL Server. SQLite uses `CREATE TABLE ... AS SELECT`.