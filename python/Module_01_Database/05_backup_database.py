import sqlite3
from config import BACKUP_DATABASE_PATH, BACKUP_DIR, DATABASE_PATH, read_statements

vacuum_into, count_rows = read_statements(__file__)

PYTHON_BACKUP_PATH = BACKUP_DIR / f"{DATABASE_PATH.stem}_python_backup.db"

# start clean: VACUUM INTO will not overwrite an existing file
BACKUP_DIR.mkdir(parents=True, exist_ok=True)
for path in (BACKUP_DATABASE_PATH, PYTHON_BACKUP_PATH):
    path.unlink(missing_ok=True)

connection = sqlite3.connect(DATABASE_PATH)

print("Backup 1: SQL (VACUUM INTO)")
connection.execute(vacuum_into, (str(BACKUP_DATABASE_PATH),))
print("Created:", BACKUP_DATABASE_PATH.name)

print("\nBackup 2: Python (connection.backup)")
copy = sqlite3.connect(PYTHON_BACKUP_PATH)
connection.backup(copy)
copy.close()
print("Created:", PYTHON_BACKUP_PATH.name)

connection.close()

print("\nCheck: rows inside each backup")
print("------------------------------")
for path in (BACKUP_DATABASE_PATH, PYTHON_BACKUP_PATH):
    check = sqlite3.connect(path)
    rows = check.execute(count_rows).fetchone()[0]
    check.close()
    print(f"{path.name}: {rows} row(s)")