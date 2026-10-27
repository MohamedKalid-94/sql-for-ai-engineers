import math
import sqlite3
from config import DATABASE_PATH, read_statements


class PopulationStdDev:
    """An aggregate for SQL: SQL calls step() once for every row, then finalize() once."""

    def __init__(self):
        self.count = 0
        self.total = 0.0
        self.total_of_squares = 0.0

    def step(self, value):
        if value is not None:
            self.count += 1
            self.total += value
            self.total_of_squares += value * value

    def finalize(self):
        if self.count < 1:
            return None
        mean = self.total / self.count
        variance = self.total_of_squares / self.count - mean * mean
        return math.sqrt(max(variance, 0.0))


class SampleStdDev(PopulationStdDev):
    """The same idea, but divides by (count - 1) because the numbers are only a sample."""

    def finalize(self):
        if self.count < 2:
            return None
        mean = self.total / self.count
        variance = (self.total_of_squares - self.count * mean * mean) / (self.count - 1)
        return math.sqrt(max(variance, 0.0))


titles = [
    "The basics: count, mean, lowest, highest and spread",
    "The median, worked out in pure SQL",
    "Standard deviation: how spread out the scores are",
    "Mean and standard deviation for each subject",
    "The three highest scores, measured in standard deviations from the mean (z-score)",
]
statements = read_statements(__file__)
assert len(titles) == len(statements), "each title needs exactly one statement"

connection = sqlite3.connect(DATABASE_PATH)
connection.create_aggregate("stddev_population", 1, PopulationStdDev)
connection.create_aggregate("stddev_sample", 1, SampleStdDev)
cursor = connection.cursor()

for number, (title, statement) in enumerate(zip(titles, statements)):
    if number:
        print()
    print(title)
    print("-" * len(title))
    cursor.execute(statement)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    if not rows:
        print("(no rows)")

connection.close()