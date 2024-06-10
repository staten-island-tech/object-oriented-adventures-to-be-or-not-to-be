n = input("do u want to start the game (Y/N) ").upper()

while n == "Y":
    location = int(input("type location number: "))
    if location == 1:
        print("this is location one")
        location = input("Do you wish to return? (Y/N) ")

    elif location == "N":
        print(":(")
            

    if location == 2:
        print("this is location two")
        location = input("Do you wish to return? (Y/N) ")

    elif location == "N":
        print(":(")