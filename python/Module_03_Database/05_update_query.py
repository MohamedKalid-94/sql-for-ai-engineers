import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""

UPDATE employees

SET salary = 75000

WHERE emp_id=101

""")

connection.commit()

print("Salary updated")

connection.close()