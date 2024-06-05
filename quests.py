import json
import os
from Player import Player
from Player import stat_checker

## Open the JSON file of inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

def quest_Jack():
    print("Quest #1 - Description: Collect 3 items, Reward: 5 XP")
    #description
    answer = input("Do you want to check quest status? (Y/N) ")
    if answer.upper() == "Y":
        if int(len(inventory)) >= 3:
            for i in Player:
                i['Total_XP'] = i['Total_XP'] + 5
                print("Jack: Congrats! You’ve successfully completed the quest -- Here’s your reward: *5 XP*")
                stat_checker()
        else:
            print("Jack: Not quite. Come back when you collect more items. ")
    else:
        input("Come back later!")

def quest_Fiona():
    print("Quest #2 - Description: Collect 5 items, Reward: 10 XP")
    #description
    answer = input("Do you want to check quest status? (Y/N) ")
    if answer.upper() == "Y":
        if int(len(inventory)) >= 5:
            for i in Player:
                i['Total_XP'] = i['Total_XP'] + 10
                print("Fiona: Nice! You finished the quest -- This is your reward: *10 XP*")
                stat_checker()
        else:
            print("Fiona: Sorry, you don't have enough items. Come back when you collect more items. ")
    else:
        input("Come back later!")

def quests_Winstell():
    print("Description: Collect 10 items, Reward: 20 XP") 
    #description
    answer = input("Do you want to check quest status? (Y/N) ")
    if answer.upper() == "Y":
        if int(len(inventory)) >= 10:
            for i in Player:
                i['Total_XP'] = i['Total_XP'] + 20
                print("Winstell: Nice job! You finished the quest -- This is your reward: *20 XP*")
                stat_checker()
        else:
            print("Winstell: You haven't completed the quest yet. Come back when you collect more items. ")
    else:
        input("Come back later!")

#change to functions that correspond to the requirement and reward given

quest_Jack()
