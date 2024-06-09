import json

## Open the JSON file of movie inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

data_dict = json.loads(inventory)

Player = [{'Name': 'name', 'Total_XP': 0, 'LVL': 0}]

def stat_checker():
    n = input("Do you want to see your stats? (Y/N) ")
    if n.upper() == "Y":
        inv = []
        print(Player)

        for item in inventory:
            for x in item:
                item = x['Name']
                inv.append(item)
                [i for i, x in enumerate(inv) if inv.count(x) > 1]
        print("Inventory: ",inv)


duplicate_counts = dict(Counter(inv))

# Print the result
print(duplicate_counts)

sorted_data_keys = json.dumps({k: data_dict[k] for k in sorted(data_dict)})
print("Sorted based on keys:", sorted_data_keys)

stat_checker()