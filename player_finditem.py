import json
## Open the JSON file of movie data
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(data)

import random

def playerfind_item(x):  #x = the range the player needs to guess -- can be used for dificulty
    number_guess = random.randint(1,int(x))
    player_guess = int(input(f"Guess a number between 1 to {x}: "))

    while player_guess != number_guess:
        print("Wrong guess")
        if player_guess < number_guess:
            print("Your guess is too low") 
        elif player_guess > number_guess:
            print("Your guess is too high")
            player_guess = int(input("Please guess again: "))

        if player_guess == number_guess:
            item_gen = random.randint(1,6)
            for i in data:
                if item_gen == i['ID']:
                    # append into player inventory
                    item = i['name']
                    item_type = i['type']
                    input("Yay! You got...")
                    print(f"Item: {item}, Type: {item_type} ")

playerfind_item(3)