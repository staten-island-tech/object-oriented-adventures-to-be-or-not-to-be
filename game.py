import json
import os
import random

## Open the JSON file of movie data
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre data list
data = json.load(data)


#**Player information

class Level:
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
                
class Name():
    def append_Name():
        def __init__(self,name):
            self.name = name
        def __str__(self):
            return f"{self.name}"
        
## Open the JSON file of movie data
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre data list
data = json.load(data)

Player = [{'Name': 'Name', 'Total_XP': 9, 'LVL': [0]}]
n = input("Do you wanna start the game (Y/N): ").upper()      
input("This is To Be or Not To be game ")

while n == "Y":
    print('Ok')
    Name = input("Please enter what you would like to be called: ")
    for i in Player:
        i['Name'] = Name
        print(f"Hello, {i['name']} The goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning!")
    location = input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " )
    if location == '1':
        input("This is Jack's Shop.")
        print("Note: You can come here for quests and to collect the items from leveling up.")
        
    elif location == "2":
        input("This is Fiona's flower shop.")
        print("Note: You can come here for information on composting and quests. You can also drop off compostable trash to fertilize her beautiful flowers.")
    elif location == "3":
        input("This is Winstell's recycling center")
        print("Note: ")
    elif location == "4":
        input("This the park.")
        print("Note: This is a place that is usually littered. You can have a higher chance of finding trash here")
    elif location == "5":
        print("This is the Beach. you can find a wider range of trash")
    elif location == "6":
        print("This is your house")
        print("Note: This is your house, you can relax here")
    elif location == "7":
        print("This is the trash can.")
    elif location == "8":
        print(Level.calc_lvl())
        print(f"These are your stats: {Player}")
    else:
        print("oh well then.")



# player find item
def find_item():  
    item_gen = random.randint(1,6)
    for i in data:
        if item_gen == i['ID']:
            # append into player inventory
            item = i['name']
            item_type = i['type']
            print(f"Item: {item}, Type: {item_type} ")

number_guess = random.randint(1,10)
player_guess = int(input("Guess a number between 1 to 10: "))

while player_guess != number_guess:
    print("Wrong guess")
    if player_guess < number_guess:
        print("Your guess is too low") 
    elif player_guess > number_guess:
      print("Your guess is too high")
    player_guess = int(input("Please guess again: "))

if player_guess == number_guess:
    input("Yay! You got...")
    find_item()
    
n = input("Would you like to change locations? (Y/N) ")



#No code needed below this line
 # Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

 # Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")