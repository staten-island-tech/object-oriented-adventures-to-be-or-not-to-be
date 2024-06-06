import json
import os
from Player import Player

## Open the JSON file of data (items)
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre data list
data = json.load(data)

## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

def calc_lvl():
    for i in Player:
        if (i['Total_XP']%8) == 0:
            y = i['Total_XP']/8
            i['LVL'] = y

        elif (i['Total_XP']-1)%8 == 0:
            y = (i['Total_XP']-1)/8
            i['LVL'] = y

        elif (i['Total_XP']-2)%8 == 0:
            y = (i['Total_XP']-2)/8
            i['LVL'] = y

        elif (i['Total_XP']-3)%8 == 0:
            y = (i['Total_XP']-3)/8
            i['LVL'] = y

        elif (i['Total_XP']-4)%8 == 0:
            y = (i['Total_XP']-4)/8
            i['LVL'] = y

        elif (i['Total_XP']-5)%8 == 0:
            y = (i['Total_XP']-5)/8
            i['LVL'] = y

        elif (i['Total_XP']-6)%8 == 0:
            y = (i['Total_XP']-6)/8
            i['LVL'] = y

        elif (i['Total_XP']-7)%8 == 0:
            y = (i['Total_XP']-7)/8
            i['LVL'] = y


n = input("Do you want to see your stats? (Y/N) ")

if n.upper() == "Y":
    print(Player)