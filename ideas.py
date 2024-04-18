import json
import os 

class Player:
    def __init__(self,Level,Name,Items):
        self.Level = Level
        self.Name = Name
        self.Items = Items
    def __str__(self):
        return f"{self.Level}, {self.Name}, {self.Items}"
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    def player(Level,Name,Xp,Items):
        player = Player(Level,Name,Xp,Items)
        data.append(player.__dict__)
        for i in data:
            print(i)

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
        for i in data:
            if i["Xp"] == 8:
                i["Level"] = (i["Level"]+1)
                data.append(i["Level"].__dict__)
                print("you leveled up: your new level is:",i["Level"])
    



            

    class Items:
        print("I")
            





#No code needed below this line
 # Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

 # Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")


