Player = [{'Name': "Judy", 'XP': 14, 'LVL': 0}]
#Player information

class rewards():
    def reward_q1():
        for i in Player:
            new = i['XP'] + 5
            i['XP'] = new
        print(Player)

    def reward_q2():
        for i in Player:
            new = i['XP'] + 10
            i['XP'] = new
        print(Player)

    def reward_q3():
        for i in Player:
            new = i['XP'] + 16
            i['XP'] = new
        print(Player)




def calc_lvl():
    for i in Player:
        print(i['XP'])
        dif = int(i['XP'])/8

        new_name = "Jessie"
        i['Name'] = new_name

        if dif.is_integer():
            print(f"You are now lvl {dif}!")
            i['LVL'] = dif

        else:
            print(f"You are now lvl {dif}!")


rewards.reward_1()
calc_lvl()
print(Player)
