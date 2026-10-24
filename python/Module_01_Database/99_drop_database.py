import os
from config import RENAMED_DATABASE_PATH

if RENAMED_DATABASE_PATH.exists():
    os.remove(RENAMED_DATABASE_PATH)
    print("Database Deleted Successfully")
else:
    print("Database not found")