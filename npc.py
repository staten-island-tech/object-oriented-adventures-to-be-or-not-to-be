class NPC(quests):
    print(quests.jacks_1())





class quests():
    
    def jacks_1():
        print("Quest #1 - Description: Collect 3 items, Reward: 5 XP")
        #description
        for i in (playerinventory.json):
            if len(playerinventory.json) == 3:

""" 

    def jacks_2():
        print("Quest #2 - Description: Collect 5 items, Reward: 10 XP")
        #description
    
    def jacks_3():
        print("Description: Collect 10 items, Reward: 20 XP")
        #description

    #change to functions that correspond to the requirement and reward given
"""  """
def choose_quest():
    import random
    select_number = random.randint(1,3)
    if select_number == 1:
        print(quests.jacks_1)

    if select_number == 2:
        print(quests.jacks_2)

    if select_number == 3:
        print(quests.jacks_3)

def npc_Jack():
    player_answer = input("Hey, I’m Jack the shopkeeper! Have you come for a quest? (Y/N)").upper()
    if player_answer == "Y":
        choose_quest()


    elif player_answer == "N":
        print("Jack: Oh well, come again later.")



















def npc_Fiona():

    def dialogue_1():

def npc_Winstell():
    print("Winstell: “Hello, I’m Winstell. If you’ve come to recycle, you arrived at the right place! Enter (A) if you would like to recycle items in your inventory, (B) to know more on items you can recycle, or (N) to cancel?")



 """