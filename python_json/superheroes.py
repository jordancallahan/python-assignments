import json

with open("superheroes.json") as f:
    superheroes = json.load(f)

powers = []

for hero in superheroes["members"]:
    powers.extend(hero["powers"])

print(powers)
