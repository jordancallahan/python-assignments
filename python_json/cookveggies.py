import json
import csv

with open("../python_csv/vegetables.csv", "r") as f:
    reader = csv.DictReader(f)
    vegetables = [row for row in reader]

with open("output/vegetables.json", "w") as f:
    json.dump(vegetables, f)
