import json

## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

Player = [{'Name': 'name', 'Total_XP': 0, 'LVL': 0}]


class stat():
    def stat_checker():
        n = input("Do you want to see your stats? (Y/N) ")
        if n.upper() == "Y":
            inv = []
            print(Player)

            for item in inventory:
                for x in item:
                    item = x['Name']
                    inv.append(item)

            print("Inventory: ",inv)

    def calc_lvl():
        for i in Player:
            if (i['Total_XP']%8) == 0:
                y = i['Total_XP']/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-1)%8 == 0:
                y = (i['Total_XP']-1)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-2)%8 == 0:
                y = (i['Total_XP']-2)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-3)%8 == 0:
                y = (i['Total_XP']-3)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-4)%8 == 0:
                y = (i['Total_XP']-4)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-5)%8 == 0:
                y = (i['Total_XP']-5)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-6)%8 == 0:
                y = (i['Total_XP']-6)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-7)%8 == 0:
                y = (i['Total_XP']-7)/8
                print(y)
                i['LVL'] = y