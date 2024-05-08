Player = [{'Name': "Judy", 'XP': 14, 'LVL': 0}]


class rewards():
    def reward_1():
        for i in Player:
            updated_xp = i['XP'] + 2
            i['XP'] = nxp
        print(Player)


def calc_lvl():
    for i in Player:
        print(i['XP'])
        dif = int(i['XP'])/8

        if dif.is_integer():
            print(f"You are now lvl {dif}!")
            i['LVL'] = dif

        else:
            print(f"You are now lvl {dif}!")


rewards.reward_1()
calc_lvl()
print(Player)









""" Player = [{'Name': "Judy", 'XP': 8, 'LVL': [10]}]


    
for i in Player:
    print(i['XP'])
    dif = int(i['XP'])/8


    if dif == [1,2,3,4,5,6,7,8,9,10]:
        print(f"You are now lvl {dif}!")
        i['LVL'].append(dif)
           

    else:
        print(f"You are lvl",i["LVL"])
       
    for i in Player:
        i['LVL'].clear()
        i['LVL'].append()
        print(Player) """

