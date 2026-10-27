# Module 09: Advanced SQL

The toolbox of larger ideas, including the attack and the defence for SQL injection.

Run: `python run_module.py 9` | Output: `outputs/Module_09_Advanced_SQL/output.txt` | Starts from: the shared tables

## Lessons

| Script | Topic |
|---|---|
| 00 create_sample_tables | removes some joining dates for the NULL lessons |
| 01 wildcards | `LIKE`, `GLOB`, `ESCAPE` |
| 02 sql_injection | the attack, and the `?` placeholder that stops it |
| 03 sql_hosting | the database file, `PRAGMA` settings, WAL mode |
| 04 min_max | smallest and largest |
| 05 null_functions | `COALESCE`, `IFNULL`, `NULLIF`, `IIF` |
| 06 check_constraint | column and row rules, each rejected on purpose |
| 07 default_constraint | `DEFAULT`, and why writing NULL does not trigger it |
| 08 stored_procedures | a Python function with named parameters, and `create_function` |
| 09 null_values | NULL maths, `COUNT`, `NULLS LAST` |
| 10 transactions | a money transfer that commits or rolls back as one unit |
| 11 sub_queries | one value, a list, a small table, and a correlated subquery |
| 12 handling_duplicates | find, delete, prevent, and `INSERT OR IGNORE` |
| 13 sequences | a counter table with `RETURNING`, and `AUTOINCREMENT` |
| 14 auto_increment | reusing an id versus never reusing it |
| 15 date_time | fixed dates, calendar maths, `strftime`, `julianday` |
| 16 cursors | `fetchone`, `fetchmany`, row by row versus set-based |
| 17 common_table_expression | `WITH` and `WITH RECURSIVE` (counting, and walking the manager tree) |
| 18 group_by_vs_order_by | folding rows versus sorting them |
| 19 in_vs_exists | and the `NOT IN` trap with NULL |
| 20 database_tuning | query plans, an index, and a calculation that hides the index |

## SQLite notes

- `RETURNING` needs SQLite 3.35.
- There are no stored procedures and no `CREATE SEQUENCE`.
- Python's `execute()` runs only one statement. `executescript()` runs several, which is why it must never receive user text.