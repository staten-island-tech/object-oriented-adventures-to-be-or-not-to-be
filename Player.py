import json

## Open the JSON file of inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

Player = [{'Name': 'Name', 'Total_XP': 0, 'LVL': 0}]

def stat_checker():
    n = input("Do you want to see your stats? (Y/N) ")

    if n.upper() == "Y":
        inv = []
        print(Player)
        for i in inventory:
            item = i["name"]
            inv.append(item)
    print("Inventory: ",inv)

stat_checker()