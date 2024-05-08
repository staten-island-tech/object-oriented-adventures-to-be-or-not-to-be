import json
import os
class Items:
    def ___init___(self,Name,Type,Id): 
            self.Name = Name
            self.Type = Type
            self.Id = Id
           
    def __str__(self):
        return f"{self.Name},{self.Type},{self.Id}"

with open("data.json", "r") as f:
# Serialize the updated Python list to a JSON string
    data = json.load(f)
##Call classes in here
    def add_item(Name,Type,Id):
        it = Items(Name,Type,Id)
        data.append(it.__dict__)
        for i in data:
            print(i)

user = input("Enter Item information Y/N?: ").upper()
while user in "Y":
    Name = input("enter name: ")
    Type = input("what type of trash it is: ")
    Id = int(input("Id number ex 1,2,3: "))

    add_item(Name,Type,Id)

    user = input("Enter Item information Y/N?: ")


    

     
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
