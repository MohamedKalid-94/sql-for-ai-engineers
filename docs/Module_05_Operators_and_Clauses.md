# Module 05: SQL Operators and Clauses

The words that shape a question: which rows, how many, in what order, grouped how.

Run: `python run_module.py 5` | Output: `outputs/Module_05_Operators_and_Clauses/output.txt` | Starts from: the shared tables

## Lessons

| Scripts | Topic |
|---|---|
| 00 | setup: a `contractors` table, David with no joining date, Alex inactive |
| 01 to 04 | `WHERE`, `LIMIT` and `OFFSET` (SQL Server's `TOP`), `DISTINCT`, `ORDER BY` |
| 05 to 06 | `GROUP BY`, `HAVING` |
| 07 to 08 | `AND`, `OR`, brackets, booleans stored as 1 and 0 |
| 09 to 10 | `LIKE`, `IN`, `NOT IN` |
| 11 to 12 | `ANY` and `ALL` (done with `MIN` and `MAX`), `EXISTS` |
| 13 | `CASE` |
| 14 to 15 | `NOT`, `<>` and `!=`, and the NULL trap |
| 16 to 18 | `IS NULL`, `IS NOT NULL`, the `NOT NULL` constraint |
| 19 | `BETWEEN` |
| 20 to 23 | `UNION`, `UNION` versus `UNION ALL`, `INTERSECT`, `EXCEPT` |
| 24 | aliases |

## Key ideas

- `= NULL` never matches. Use `IS NULL`.
- `COUNT(*)` counts rows, `COUNT(column)` skips NULLs.
- `LIKE` ignores letter case in SQLite.