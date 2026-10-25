import sqlite3
from config import DATABASE_PATH

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


cursor.execute("""
DROP TABLE IF EXISTS employee_constraints
""")


cursor.execute("""

CREATE TABLE employee_constraints(

    emp_id INTEGER PRIMARY KEY,

    employee_code TEXT UNIQUE,

    name TEXT NOT NULL,

    salary REAL
        CHECK(salary >= 0),

    department TEXT
        DEFAULT 'General'

)

""")


print("employee_constraints table created\n")


cursor.execute("""

INSERT INTO employee_constraints
(emp_id, employee_code, name, salary)

VALUES

(1,'EMP001','John',70000)

""")


cursor.execute("""

INSERT INTO employee_constraints
(emp_id, employee_code, name, salary)

VALUES

(2,'EMP002','Sara',85000)

""")


connection.commit()


print("Sample records inserted\n")


cursor.execute("""

SELECT *

FROM employee_constraints

""")


rows = cursor.fetchall()


for row in rows:

    print(row)


connection.close()