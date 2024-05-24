import json
import os
from Player import Player

with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

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



for i in Player:
    i['Name'] = "Judy"
    i['Total_XP'] = 15
    calc_lvl()

""" 
for i in data:
    if i["type"] == "Compostable":
        add = i["name"]
        for i in Player:
            i['INV'].append(add) """
        
        
n = input("Do you want to see your stats? (Y/N) ")

if n.upper() == "Y":
    print(Player)
        
""" for i in data:
    if i["type"] == "Recyclable":
        add = i["name"]
        for i in Player:
            i['INV'].append(add)
         """
        
        
n = input("Do you want to see your stats? (Y/N) ")

if n.upper() == "Y":
    for i in Player:
        print(i['Name'], i['Total_XP'], i['LVL'], i['INV'])