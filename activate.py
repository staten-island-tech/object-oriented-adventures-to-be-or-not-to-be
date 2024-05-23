Player = [{'Name': "Judy", 'XP': 14, 'LVL': [0]}]


class rewards():
    def reward_1():
        for i in Player:
            nxp = i['XP'] + 2
            i['XP'] = nxp
        print(Player)


class Level:
    def calc_lvl():
        for i in Player:
            if (i['Total_XP']%8) == 0:
                y = i['Total_XP']/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-1)%8 == 0:
                y = (i['Total_XP']-1)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-2)%8 == 0:
                y = (i['Total_XP']-2)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-3)%8 == 0:
                y = (i['Total_XP']-3)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-4)%8 == 0:
                y = (i['Total_XP']-4)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-5)%8 == 0:
                y = (i['Total_XP']-5)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-6)%8 == 0:
                y = (i['Total_XP']-6)/8
                print(y)
                i['LVL'] = y
            elif (i['Total_XP']-7)%8 == 0:
                y = (i['Total_XP']-7)/8
                print(y)
                i['LVL'] = y 






