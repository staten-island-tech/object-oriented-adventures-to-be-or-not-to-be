import json
import os


with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

Player = [{'Name': 'Name', 'Total_XP': 0, 'LVL': 0, 'INV':[]}]

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


for i in Player:
    i['Name'] = "Judy"
    i['Total_XP'] = 17
    calc_lvl()
print(Player)


for i in data:
    if i["type"] == "Trash":
        add = i["name"]
        for i in Player:
            i['INV'].append(add)
        
        
        
n = input("Do you want to see your stats? ")

if n.upper() == "Y":
    print(Player)
        
for i in data:
    if i["type"] == "Recyclable":
        add = i["name"]
        for i in Player:
            i['INV'].append(add)
        
        
        
n = input("Do you want to see your stats? ")

if n.upper() == "Y":
    print(Player)
        