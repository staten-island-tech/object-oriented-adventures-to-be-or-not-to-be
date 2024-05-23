import json
import os

with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here


Player = [{'Name': 'Name', 'Total_XP': 0, 'LVL': 0, 'INV':[]}]

for i in data:
    if i["type"] == "Recyclable":
        Player.append(i['name'])
        print(Player)

** WIP