import json
import os
class Items:
    def Inventory():
        def ___init___(self,Plastic_Bottles,Plastic_Bag,Empty_Food_Wrapper,Empty_Soda_Can,Banana_Peel,Styrofoam_Packet): 
            self.Plastic_Bottles = Plastic_Bottles
            self.Plastic_Bag = Plastic_Bag
            self.Empty_Food_Wrapper = Empty_Food_Wrapper
            self.Empty_Soda_Can = Empty_Soda_Can
            self.Banana_Peel = Banana_Peel
            self.Styrofoam_Packet = Styrofoam_Packet
        def __str__(self):
            return f"{self.Plastic_Bottles}, {self.Plastic_Bag}, {self.Empty_Food_Wrapper}, {self.Empty_Soda_Can}, {self.Banana_Peel}, {self.Styrofoam_Packet}"
with open("data.json", "r") as f:
# Serialize the updated Python list to a JSON string
    data = json.load(f)
##Call classes in here
    def add_item(Plastic_Bottles,Plastic_Bag,Empty_Food_Wrapper,Empty_Soda_Can,Banana_Peel,Styrofoam_Packet):
        items = Items(Plastic_Bottles,Plastic_Bag,Empty_Food_Wrapper,Empty_Soda_Can,Banana_Peel,Styrofoam_Packet)
        data.append(items.__dict__)
        for i in data:
            print(i)
print("You found a ")
pick_up = input("Please type this : ")
data.append(pick_up)
print(data)



                
        





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