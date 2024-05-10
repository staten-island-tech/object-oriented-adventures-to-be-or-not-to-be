import json
import os

class Name:
    def append_Name():
        def __init__(self,name):
            self.name = name
        def __str__(self):
            return f"{self.name}"

with open("player.json", "r") as f:
# Serialize the updated Python list to a JSON string
    player = json.load(f)
##Call classes in here
Player = [{'Name': Name, 'XP': 0, 'LVL': [0]}]
print("this is to be or to not be game")
n = input("Do you wanna start the game Y/N: ").upper()      


while n == "Y":
    print('Ok')
    Name = input("Please enter what you would like to be called: ")
    Player.append(Name)
    print("Hello,",Name,"The goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning experience.")
    location = input("You have 6 available locations to go to. Type the number of one of the following: 1.Jack's shop, 2.Fiona's flower shop, 3.Winstell's recycling center, 4.Park, 5.Beach, 6.House, 7.Trash can: " )
    if location == '1':
        print("This is Jack's Shop.")
        print("Note: You can come here for quests and to collect the items from leveling up.")
        print(Player)
    elif location == "2":
        print("This is Fiona's flower shop.")
        print("Note: You can come here for information on composting and quests. You can also drop off compostable trash to fertilize her beautiful flowers.")
    elif location == "3":
        print("This is Winstell's recycling center")
        print("Note: ")
    elif location == "4":
        print("This the park.")
        print("Note: This is a place that is usually littered. You can have a higher chance of finding trash here")
    elif location == "5":
        print("This is the Beach. you can find a wider range of trash")
    elif location == "6":
        print("This is your house")
        print("Note: This is your house, you can relax here")
    elif location == "7":
        print("This is the trash can.")
    else:
        print("oh well then.")

class Level:
    

    def calc_lvl():
        Player = [{'Name': "Judy", 'XP': 17, 'LVL': [10]}]
        quotient = []
        for i in Player:
            print(i['XP'])
            dif = int(i['XP'])/8


            quotient.append(int(dif))


            if dif.is_integer():
                print(f"You are now lvl {dif}!")
                i['LVL'].append(dif)
           


            else:
                print(f"You are now lvl {dif}!")
       
        for i in Player:
            i['LVL']=dif
            print(Player)







#No code needed below this line
 # Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(player)

    # Write the JSON string to the new JSON file
    f.write(json_string)

 # Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")