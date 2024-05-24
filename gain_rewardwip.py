import Player

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
