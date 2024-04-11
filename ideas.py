print("this is to be or to not be game")
n = input("Do you wanna start the game Y/N: ").upper()

while n == "Y":
    print('Ok')
    name = input("Please enter what you would like to be called: ")
    print("hello,",name,"The goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning experience.")
    location = input("You have 6 avaliable locations to go to. Type the number of one of the following: 1.Jack's shop, 2.Fiona's flower shop, 3.Winstell's recycling center, 4.Park, 5.Beach, 6.House: " )
    if location == '1':
        print("This is Jack's Shop.")
        print("Note: You can come here for quests and to collect the items from the level up")
        o = input("Would you like to talk to Jack: Y/N").upper()
        if o == "Y":
            h = ("Hey, I am Jack, the shopkeeper! Have you come for a quest? (Y/N) ").upper()
        else:
            location = input("You have 6 avaliable locations to go to. Type the number of one of the following: 1.Jack's shop, 2.Fiona's flower shop, 3.Winstell's recycling center, 4.Park, 5.Beach, 6.House: " )
    if location == "2":
        print("This is Fiona's flower shop")
        print("Note:")
else:
    print("oh well then.")
