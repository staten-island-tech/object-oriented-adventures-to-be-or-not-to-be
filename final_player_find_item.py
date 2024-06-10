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

def guess(x):
    ask = input("Do you want to search for trash? (Y/N) ")
    while ask.upper() == "Y":
        r = [("1"),("2"),("3"),("4"),("5"),("6"),("7"),("8"),("9"),("10")]
        number_guess = random.randint(1,10)
        player_guess = input("Guess a number between 1 to 10: ")

        if player_guess in r:
            while int(player_guess) != number_guess:
                if int(player_guess) < number_guess:
                    print("Wrong guess: Your guess is too low") 
                elif int(player_guess) > number_guess:
                    print("Wrong guess: Your guess is too high")     
                player_guess = int(input("Please guess again: "))
        
            if int(player_guess) == number_guess:
                    item_gen = random.randint(1,x)

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

                                ask = input("Do you want to search for trash? (Y/N) ")
        else:
            print("Error--")
            ask = input("Do you want to search for trash? (Y/N) ")

    else:
        print("Oh well..")
