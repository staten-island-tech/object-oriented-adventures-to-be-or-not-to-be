import json
## Open the JSON file of movie data
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(data)


import random

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
    
        
        



"""
class rewards():
    def reward_1():
        for i in Player:
            i['total_XP'] = i['total_XP'] + 2
            print(i['total_XP'])




class Level:

    def calc_lvl():
        for i in Player:
            if (i['total_XP']%8) == 0:
                y = i['total_XP']/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-1)%8 == 0:
                y = (i['total_XP']-1)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-2)%8 == 0:
                y = (i['total_XP']-2)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-3)%8 == 0:
                y = (i['total_XP']-3)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-4)%8 == 0:
                y = (i['total_XP']-4)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-5)%8 == 0:
                y = (i['total_XP']-5)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-6)%8 == 0:
                y = (i['total_XP']-6)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-7)%8 == 0:
                y = (i['total_XP']-7)/8
                print(y)
                i['LVL'] = y

rewards.reward_1()
"""