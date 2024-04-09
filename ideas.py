print("this is to be or to not be game")
n = input("Do you wanna start the game Y/N: ").upper()

if n == "Y":
    print('ok')
    name = input("please enter what you would like to be called: ")
    print("hello,",name,"the goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning experiance.")
    location = input("you have 7 avalible locations to go to. Type one of the following: Trash can, Jack's shop, Fiona's flower shop, Winstell's recycling center, park, beach, and finally house: " ).lower()
    if location == 'trash can':
        print("this is the trash can, you can drop off all kinds of trash but it doesnt give you any xp. It is recommended that only non recyclable trash and non compostable trash be dropped off here.")
        location = input("you have 6 avalible locations to go to. Type one of the following: Jack's shop, Fiona's flower shop, Winstell's recycling center, park, beach, and finally house: " ).lower()
    if location == "jack's shop":
        print("one")
else:
    print("oh well then.")
