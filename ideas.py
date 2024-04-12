print("this is to be or to not be game")
n = input("Do you wanna start the game Y/N: ").upper()

while n == "Y":
    print('Ok')
    name = input("Please enter what you would like to be called: ")
    print("Hello,",name,"The goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning experience.")
    location = input("You have 6 available locations to go to. Type the number of one of the following: 1.Jack's shop, 2.Fiona's flower shop, 3.Winstell's recycling center, 4.Park, 5.Beach, 6.House, 7.Trash can: " )
    if location == '1':
        print("This is Jack's Shop.")
        print("Note: You can come here for quests and to collect the items from leveling up.")
        o = input("Would you like to talk to Jack: Y/N").upper()
        if o == "Y":
            h = ("Hey, I am Jack, the shopkeeper! Have you come for a quest? (Y/N) ").upper()
        else:
            location = input("You have 6 available locations to go to. Type the number of one of the following: 1.Jack's shop, 2.Fiona's flower shop, 3.Winstell's recycling center, 4.Park, 5.Beach, 6.House 7.Trash can: " )
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
        print("Note: This is your house, you can check if the things in your house is recyclable")
    if location == "7":
        print("This is the trash can.")
else:
    print("oh well then.")
