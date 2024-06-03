import Player
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


rewards.reward_1()
calc_lvl()
print(Player)
