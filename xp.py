import json
## Open the JSON file of movie data
data = open("./data.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(data)

for i in data:
    if i['ID'] == 2:
        print(i['name'])


"""
class rewards():
    def reward_1():
        for i in Player:
            i['total_XP'] = i['total_XP'] + 2
            print(i['total_XP'])




class Level:

    def calc_lvl():
        for i in Player:
            if (i['total_XP']%8) == 0:
                y = i['total_XP']/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-1)%8 == 0:
                y = (i['total_XP']-1)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-2)%8 == 0:
                y = (i['total_XP']-2)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-3)%8 == 0:
                y = (i['total_XP']-3)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-4)%8 == 0:
                y = (i['total_XP']-4)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-5)%8 == 0:
                y = (i['total_XP']-5)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-6)%8 == 0:
                y = (i['total_XP']-6)/8
                print(y)
                i['LVL'] = y
            elif (i['total_XP']-7)%8 == 0:
                y = (i['total_XP']-7)/8
                print(y)
                i['LVL'] = y

rewards.reward_1()
"""