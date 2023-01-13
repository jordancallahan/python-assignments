import json
import csv

with open("superheroes.json") as f:
    superheroes = json.load(f)

with open("superheroes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(
        [
            "name",
            "age",
            "secretIdentity",
            "powers",
            "squadName",
            "homeTown",
            "formed",
            "secretBase",
            "active",
        ]
    )
    for superhero in superheroes["members"]:
        writer.writerow(
            [
                superhero["name"],
                superhero["age"],
                superhero["secretIdentity"],
                superhero["powers"],
                superheroes["squadName"],
                superheroes["homeTown"],
                superheroes["formed"],
                superheroes["secretBase"],
                superheroes["active"],
            ]
        )
