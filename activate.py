#Call class from here
from game import Player
Player = [{'Name': 'Name', 'Total_XP': 0, 'LVL': 0}]

""" class rewards():  WIP***
    def reward_1():
        for i in Player:
            nxp = i['XP'] + 2
            i['XP'] = nxp
        print(Player) """


class Name():
    def append_Name():
        def __init__(self,name):
            self.name = name
        def __str__(self):
            return f"{self.name}

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
    print(f"Item: {item}, Type: {item_type} ")