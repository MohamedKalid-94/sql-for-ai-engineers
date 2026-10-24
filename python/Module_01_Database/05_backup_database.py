import shutil
from config import RENAMED_DATABASE_PATH, BACKUP_DATABASE_PATH

if RENAMED_DATABASE_PATH.exists():
    shutil.copy(
        RENAMED_DATABASE_PATH,
        BACKUP_DATABASE_PATH
    )
    print("Backup Completed Successfully")

else:
    print("Database not found")