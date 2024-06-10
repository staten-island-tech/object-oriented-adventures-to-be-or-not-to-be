import json
from Player import Player
from Player import stat
from final_player_find_item import guess
from quests import NPC


## Open the JSON file of data (items)
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre data list
data = json.load(data)

## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

    
n = input("Do you wanna start the game (Y/N): ").upper()      
print("This is To Be or Not To be game ")
User = input("Enter Username: ")
for i in Player:
    i['Name'] = User
    print(f"Hello, {i['Name']} The goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning!")
while n == "Y":
    
    location = int(input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " ))
    if location == 1:
        input("This is Jack's Shop.")
        print("Note: You can come here for quests and to collect the items from leveling up.")
        quest_ask = input("Would you like to see Jack's quest? (Y/N) ")
        if quest_ask.upper() == "Y": 
            for i in inventory: 
                print(NPC.quest_Jack())
        
    elif location == 2:
        input("This is Fiona's flower shop.")
        print("Note: You can come here for information on composting and quests. You can also drop off compostable trash to fertilize her beautiful flowers.")
        quest_ask = input("Would you like to start Fiona's quest? (Y/N) ")
        if quest_ask.upper() == "Y":  
            print(NPC.quest_Fiona())
        location = int(input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " ))


    elif location == 3:
        input("This is Winstell's recycling center")
        print("Note from planet Earth: Recycling the wrong materials will cause harm to OUR environment ")
        quest_ask = input("Would you like to start Winstell's quest? (Y/N) ")
        if quest_ask.upper() == "Y":  
            print(NPC.quests_Winstell())
        

    elif location == 4:
        input("This the park.")
        print("Note: This is a place that is usually littered. Please help clean our littered parks.")
        locations = input("Would you like to change locations?(Y/N) ").upper()

        while locations == "N":
                #ask player if they want to find item
            guess(5)
            locations = input("Would you like to change locations? (Y/N) ").upper()
            if locations == "Y":
                location = int(input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " ))
                

    elif location == 5:
        print("This is the Beach. you can find a wider range of trash")
        guess(8)
        
           
         
        
    elif location == 6:
        print("This is your house")
        print("Note: This is your house, you can relax here")

    elif location == 7:
        print("This is the trash can.")

    elif location == 8:
        print(stat.calc_lvl())
        print(stat.stat_checker())
    else:
        print("--An error occurred--")
        
else:
        print("oh well then.")

