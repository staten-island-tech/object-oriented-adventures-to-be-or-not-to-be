# ** TESTING

import json
import os
import random

## Open the JSON file of data (items)
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre data list
data = json.load(data)

## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

class Player:
    Player = [{'Name': 'Name', 'Total_XP': 9, 'LVL': [0]}]

class find_item:

    def guess():
        number_guess = random.randint(1,10)
        player_guess = int(input("Guess a number between 1 to 10: "))

        while player_guess != number_guess:
            if player_guess < number_guess:
                print("Wrong guess: Your guess is too low") 
            elif player_guess > number_guess:
                print("Wrong guess: Your guess is too high")
            player_guess = int(input("Please guess again: "))
        
        if player_guess == number_guess:
                item_gen = random.randint(1,8)

                for i in data:
                    if item_gen == i['ID']:
                        item = i['name']
                        item_type = i['type']
                        input("Yay! You got...")
                        print(f"Item: {item}, Type: {item_type} ")
                        
                        add_item = [{'Name': [], 'ID': 0}]
                        for i in add_item:
                            i['Name'] = item
                            i['ID'] = item_gen
                            inventory.append(add_item)
                        

#ask player
ask = input("Do you want to search for an item? (Y/N) ")
while ask.upper() == "Y":
    find_item.guess()
    ask = input("Do you want to search for an item? (Y/N) ")
    print(f"This is your inventory: {inventory}")
else:
    print("Oh well..")




# Creates a new JSON file with the updated inventory
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(inventory)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("inventory.json")
os.rename(new_file, "inventory.json")