import json

## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

Player = [{'Name': 'name', 'Total_XP': 0, 'LVL': 0}]

def stat_checker():
    n = input("Do you want to see your stats? (Y/N) ")
    inv = []
    if n.upper() == "Y":
        print(Player)
        for i in inventory:
            x = i["Name"]
            print(x)
        inv.append()
        print("Inventory: ",inventory)

stat_checker()