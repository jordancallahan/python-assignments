import csv
import json

green_veggies = []

with open("../python_csv/vegetables.csv", "r") as f:
    reader = csv.DictReader(f)
    veggies = [row for row in reader]
    for row in veggies:
        if row["color"] == "green":
            green_veggies.append(row)

with open("output/greenveggies.json", "w") as f:
    json.dump(green_veggies, f)

with open("output/green_vegetables.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=green_veggies[0].keys())
    writer.writeheader()
    writer.writerows(green_veggies)
