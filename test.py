n = input("do u want to start the game").upper()

if n == "Y":
    location = int(input("1,2"))
    while location == 1:
        if location == 1:
            print("i")
            location = int(input("1,2"))
        elif location == "2":
            print("hi)")
            location = int(input("1,2"))
else:
    print("oh well")