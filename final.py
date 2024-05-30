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

def guess():
    ask = input("Do you want to search for trash? (Y/N) ")
    while ask.upper() == "Y":
        number_guess = random.randint(1,10)
        player_guess = int(input("Guess a number between 1 to 10: "))

        while player_guess == (1,2,3,4,5,6,7,8,9,10):
            guess = (player_guess)
            while guess != number_guess:
                if guess < number_guess:
                    print("Wrong guess: Your guess is too low") 
                elif guess > number_guess:
                    print("Wrong guess: Your guess is too high")     
                guess = int(input("Please guess again: "))
            player_guess = input("Please guess a number between 1 to 10: ")

        if player_guess != (1,2,3,4,5,6,7,8,9,10):
            player_guess = int(input("Please guess a number between 1 to 10: "))

        
        
        if guess == number_guess:
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


ask = input("Do you want to search for trash? (Y/N) ")
print(f"This is your inventory: {inventory}")

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