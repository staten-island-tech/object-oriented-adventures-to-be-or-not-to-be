import json
import os 


print("this is to be or to not be game")
n = input("Do you wanna start the game Y/N: ").upper()
class Name:
        if n == "Y":
            print('Ok')
            Name = input("Please enter what you would like to be called: ")
            print("Hello,",Name,"The goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning experience.")
            location = input("You have 6 available locations to go to. Type the number of one of the following: 1.Jack's shop, 2.Fiona's flower shop, 3.Winstell's recycling center, 4.Park, 5.Beach, 6.House, 7.Trash can: " )
            if location == '1':
                print("This is Jack's Shop.")
                print("Note: You can come here for quests and to collect the items from leveling up.")
            if location == "2":
                print("This is Fiona's flower shop.")
                print("Note: You can come here for information on composting and quests. You can also drop off compostable trash to fertilize her beautiful flowers.")
            if location == "3":
                print("This is Winstell's recycling center")
                print("Note: ")
            if location == "4":
                print("This the park.")
                print("Note: This is a place that is usually littered. You can have a higher chance of finding trash here")
            if location == "5":
                print("This is the Beach. you can find a wider range of trash")
            if location == "6":
                print("This is your house")
                print("Note: This is your house, you can relax here")
            if location == "7":
                print("This is the trash can.")
        else:
            print("oh well then.")
class Level:
    Player = [{'Name': "Judy", 'XP': 17, 'LVL': [10]}]

    def calc_lvl():
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
        i['LVL'].clear()
        i['LVL'].append(1)
        print(Player)



    



            

class Items:
        print("I")
            





