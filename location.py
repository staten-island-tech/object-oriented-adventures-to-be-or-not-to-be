from Player import Player

import json
from Player import Player
from calc_lvl import calc_lvl
from final_player_find_item import guess

## Open the JSON file of data (items)
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre data list
data = json.load(data)

## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)



class location():
    def one():
        if location == '1':
            input("This is Jack's Shop.")
            print("Note: You can come here for quests and to collect the items from leveling up.")
            location = input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " )
    def two():
        if location == "2":
            input("This is Fiona's flower shop.")
            print("Note: You can come here for information on composting and quests. You can also drop off compostable trash to fertilize her beautiful flowers.")
    def three():
        if location == "3":
            input("This is Winstell's recycling center")
            print("Note: Winstell will only take recyclable items, if an item that is given to him is non recyclable, XP will be dropped. Please be careful. ")
            print("Note from planet Earth: Recycling the wrong materials will cause harm to OUR environment ")
    def four():
        if location == "4":
            input("This the park.")
            print("Note: This is a place that is usually littered. Please help clean our littered parks.")
            locations = input("Would you like to change locations?(Y/N) ").upper()

            while locations == "N":
                #ask player if they want to find item
                    guess()
                    print(f"This is your inventory: {inventory}")
                    locations = input("Would you like to change locations? (Y/N) ").upper()
                    if locations == "Y":
                        location = input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " )

    
    def five():
        if location == "5":
            print("This is the Beach. you can find a wider range of trash")
            while location == "N":
                #ask player if they want to find item
                ask = input("Do you want to search for trash? (Y/N) ")
                while ask.upper() == "Y":
                    guess()
                    ask = input("Do you want to search for trash? (Y/N) ")
                    print(f"This is your inventory: {inventory}")
                else:
                    print("Oh well..")


            location = input("Would you like to change locations? (Y/N) ").upper()
            if location == "Y":
                location = input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " )
        
    def six():        
        if location == "6":
            print("This is your house")
            print("Note: This is your house, you can relax here")
    def seven():
        if location == "7":
            print("This is the trash can.")

    def eight():
            if location == "8":
                print(calc_lvl())
                print(f"These are your stats: {Player}")