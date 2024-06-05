from Player import Player

def calc_lvl():
    for i in Player:
        if (i['Total_XP']%8) == 0:
            y = i['Total_XP']/8
            i['LVL'] = y

        elif (i['Total_XP']-1)%8 == 0:
            y = (i['Total_XP']-1)/8
            i['LVL'] = y

        elif (i['Total_XP']-2)%8 == 0:
            y = (i['Total_XP']-2)/8
            i['LVL'] = y

        elif (i['Total_XP']-3)%8 == 0:
            y = (i['Total_XP']-3)/8
            i['LVL'] = y

        elif (i['Total_XP']-4)%8 == 0:
            y = (i['Total_XP']-4)/8
            i['LVL'] = y

        elif (i['Total_XP']-5)%8 == 0:
            y = (i['Total_XP']-5)/8
            i['LVL'] = y

        elif (i['Total_XP']-6)%8 == 0:
            y = (i['Total_XP']-6)/8
            i['LVL'] = y

        elif (i['Total_XP']-7)%8 == 0:
            y = (i['Total_XP']-7)/8
            i['LVL'] = y