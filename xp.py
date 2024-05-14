Player = [{'Name': "Judy", 'total_XP': 0, 'LVL': 0}]



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