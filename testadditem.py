import json
import os
## Create Class for creating new dictionaries here

class Items():
    def __init__(self,name, type, ID):
        self.name = name
        self.type = type
        self.ID = ID
         
    def __str__(self):
        return f"{self.name}, {self.type}, {self.ID}"



with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

    def create_item(name, type, ID):
        new_item = Items(name, type, ID)
        data.append(new_item.__dict__)
        for i in data:
            print(i)



user_inp = input("Do you want input a new Item? (Y/N) ").upper()

while user_inp == "Y":
    name = (input("Enter item name: "))
    type = (input("Enter item type: "))
    ID = (int(input("Enter ID (integer): ")))

    create_item(name,type,ID)

    user_inp = input("Do you want to input another Item? (Y/N) ").upper()
    



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