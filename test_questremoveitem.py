
import json


## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)


def should_delete(item):
    return item['key'] == 'value_to_delete'

# Filter out items that meet the deletion condition
data = [item for item in inventory if not should_delete(item)]