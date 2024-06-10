# Welcome to the main game code!!! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧

from Player import Player


n = input("Do you wanna start the game (Y/N): ").upper()      
print("This is To Be or Not To be game ")

while n == "Y":
    print('Ok')
    User = input("Enter Username: ")
    for i in Player:
        i['Name'] = User
        print(f"Hello, {i['Name']} The goal of this game is to collect littered trash and learn about the best place to drop it off. This game is interactive and a great, fun learning!")
    location = input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " )
    if location == '1':
        location.one()
    if location =='2':
        location.two()
    if location =='3':
        location.three()
    if location =='4':
        location.four()
    if location =='5':
        location.five()
    if location =='6':
        location.six()
    if location =='7':
        location.seven()
            
    else:
        print("nevermind..")