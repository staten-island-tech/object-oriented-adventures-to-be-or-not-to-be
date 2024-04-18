import json
import os 
with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

class Level:
    for i in data:
       print(i["Level"])


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

