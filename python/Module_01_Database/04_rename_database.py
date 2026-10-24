import os
from config import DATABASE_PATH, RENAMED_DATABASE_PATH


if DATABASE_PATH.exists():
    os.rename(DATABASE_PATH, RENAMED_DATABASE_PATH)
    print("Database Renamed Successfully")
else:
    print("Database not found")