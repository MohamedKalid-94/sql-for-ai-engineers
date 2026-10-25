import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("""
DROP TABLE IF EXISTS employees_clustered;
""")


cursor.execute("""
CREATE TABLE employees_clustered AS
SELECT *
FROM employees
ORDER BY emp_id;
""")


print("Clustered Index Equivalent Table")
print("--------------------------------")


cursor.execute("""
SELECT emp_id, emp_name, salary
FROM employees_clustered;
""")


for row in cursor.fetchall():
    print(row)


connection.close()