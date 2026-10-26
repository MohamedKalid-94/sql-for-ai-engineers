import os
import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# run_module.py sets DATABASE_PATH so each module gets its own fresh database.
# Running a script by hand uses database/company.db instead.
DATABASE_PATH = Path(
    os.environ.get("DATABASE_PATH", PROJECT_ROOT / "database" / "company.db")
)

RENAMED_DATABASE_PATH = DATABASE_PATH.with_name(DATABASE_PATH.stem + "_archive.db")

BACKUP_DIR = DATABASE_PATH.parent / "backup"
BACKUP_DATABASE_PATH = BACKUP_DIR / f"{DATABASE_PATH.stem}_backup.db"


def get_connection(path=None):
    """Open a connection with foreign keys enforced (used by Module 5 and later)."""
    target = Path(path) if path else DATABASE_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(target)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def read_statements(script_file):
    """Return the SQL statements from the .sql file that matches this script.

    python/Module_01_Database/01_create_database.py
        -> sql/Module_01_Database/01_create_database.sql
    The statements come back in the same order they appear in the file.
    """
    script = Path(script_file).resolve()
    relative = script.relative_to(PROJECT_ROOT / "python")
    sql_file = PROJECT_ROOT / "sql" / relative.with_suffix(".sql")

    statements, buffer = [], ""
    for line in sql_file.read_text(encoding="utf-8-sig").splitlines():
        buffer += line + "\n"
        if sqlite3.complete_statement(buffer):   # True once a statement ends with ;
            statements.append(buffer.strip())
            buffer = ""
    return statements