import json
from Player import Player

def stat_checker():

    import json

    ## Open the JSON file of inventory
    inventory = open("./inventory.json", encoding="utf8")
    ## create variable "inventory" that represents the enitre inventory list
    inventory = json.load(inventory)


    n = input("Do you want to see your stats? (Y/N) ")

    if n.upper() == "Y":
        inv = []
        print(Player)
        for m in inventory:
                inv.append(m["title"])
        print("Inventory: ", inv)
stat_checker()
