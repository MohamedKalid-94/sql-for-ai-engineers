# Contributing

Thank you for helping. This repository teaches SQL through small lessons that run, so every change must keep the whole course runnable.

## Set up

```bash
git clone https://github.com/MohamedKalid-94/sql-for-ai-engineers.git
cd sql-for-ai-engineers
python run_module.py --all
```

Python 3.12 and SQLite 3.35 or newer are needed. Nothing else is installed.

## How a lesson is built

Each lesson is two files with the same name in matching folders:

```text
sql/Module_06_Joins/03_left_join.sql
python/Module_06_Joins/03_left_join.py
```

- The `.sql` file holds the queries. The `.py` file loads them with `read_statements(__file__)` from `python/config.py` and runs them.
- Statements come back in file order, so the names unpacked in the `.py` file must follow the same order.
- Never put a semicolon inside a `.sql` comment. A semicolon is how a statement end is found.
- File names start with two digits (`00_`, `01_`, ...). The runner ignores any other name, and any name starting with `98` or `99`.

## Rules for a lesson

1. **Deterministic.** Use fixed dates and add `ORDER BY` wherever row order shows. Do not print `date('now')`, timings, or random values.
2. **No local paths.** Print `path.name`, never a full path.
3. **Prove the idea.** Show a result, and show a rejection when the lesson is about a rule. Mark a statement that is meant to fail with `REJECTED ON PURPOSE` in its comment, and catch the error in the `.py` file.
4. **Named columns.** Write `INSERT INTO t (a, b)` and `SELECT a, b`, not `SELECT *`, unless the lesson is about `*`.
5. **Parameters.** Put values in with `?` placeholders or `:name`, never by pasting text into SQL (except the lesson that shows why not).
6. **SQLite only.** If a command exists in MySQL or SQL Server but not in SQLite, show what SQLite does instead, and say so in a comment.
7. **Own database.** Never rely on another module's data. Modules 3 and later start from `sql/common/schema.sql` and `seed.sql`.

## Before you open a pull request

```bash
python run_module.py --all
python run_module.py --all
git diff --stat outputs
```

- Both runs must end with `All scripts completed successfully`.
- The second run must change nothing in `outputs/`.
- The output must contain no machine paths: search `outputs` for a drive letter like `C:\`.
- Update `docs/<module>.md` and `CHANGELOG.md` when you add or change a lesson.

## Commit messages

Use a short prefix: `feat:` for a new lesson or module, `fix:` for a bug, `docs:` for text, `chore:` for housekeeping.

## Reporting a problem

Open an issue with your Python and SQLite versions (`python -c "import sys, sqlite3; print(sys.version, sqlite3.sqlite_version)"`), the command you ran, and the part of `outputs/<module>/output.txt` that shows the error.