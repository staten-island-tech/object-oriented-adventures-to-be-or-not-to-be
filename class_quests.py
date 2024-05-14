Player = [{'Name': "Judy", 'total_XP': 0, 'LVL': 0}]

class quests():
    def quest_Jack():
        print("Quest #1 - Description: Collect 3 items, Reward: 5 XP")
        #description

    def quest_Fiona():
        print("Quest #2 - Description: Collect 5 items, Reward: 10 XP")
        #description
    
    def quests_Winstell():
        print("Description: Collect 10 items, Reward: 20 XP") 
        #description

    #change to functions that correspond to the requirement and reward given

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
