Player = [{'Name': "Judy", 'XP': 14, 'LVL': 0}]


class rewards():
    def reward_1():
        for i in Player:
            nxp = i['XP'] + 2
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
