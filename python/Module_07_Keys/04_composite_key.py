import sqlite3
from config import DATABASE_PATH


connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


cursor.execute("""
DROP TABLE IF EXISTS employee_projects
""")


cursor.execute("""
CREATE TABLE employee_projects
(
    emp_id INTEGER,
    project_id INTEGER,

    PRIMARY KEY(emp_id, project_id)
)
""")


data = [

(101,1),
(101,2),
(102,1)

]


cursor.executemany(
"""
INSERT INTO employee_projects
VALUES (?,?)
""",
data
)


connection.commit()


print("COMPOSITE KEY Result")
print("--------------------")


for row in cursor.execute(
    "SELECT * FROM employee_projects"
):
    print(row)


connection.close()