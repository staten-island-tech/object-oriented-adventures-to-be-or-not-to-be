import json
import os 

class Player:
    def __init__(self,Level,Name,Xp,Items):
        self.Level = Level
        self.Name = Name
        self.Xp = Xp
        self.Items = Items
    def __str__(self):
        return f"{self.Level}, {self.Name}, {self.Xp}, {self.Items}"
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here
    def create_actor(Level,Name,Xp,Items):
        player = Player(Level,Name,Xp,Items)
        data.append(player.__dict__)
        for i in data:
            print(i)



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