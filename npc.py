****** NOT UPDATED!!!*****















answer = input("Do you want to visit Jack? Y/N ")
if answer.upper() == "Y":
    return True
else:
    confirm == False


class NPC():
    def __init__(info, name, location, description, dialogue):
        info.name = name
        info.location = location
        info.description = description
        info.dialogue = dialogue

class jack():
    def __init__(info, name, location, description, dialogue):
        name = "Jack"
        location = "Shopkeeper"
        description = "Jack is a shopkeeper whose shop is alway littered, he can give quests and if you complete them, a reward will be given such as xp."
        dialogue = input("Hey, I’m Jack the shopkeeper! Have you come for a quest? (Y/N)")
        super(NPC).__init__(name, location, description, dialogue)

    def action(dialogue):
        if dialogue.upper() == "Y":
            print(quests.quest_Jack())
            
        elif dialogue.upper() == "N":
            print("Jack: Oh well, come again next time.")
            continue_jack == False


""" 
class Fiona():
    name = "Fiona"
    location = "Flower Shop Keeper"
    description = "Fiona is only unlocked after level 1 and she owns a flower shop where you can drop off compostable things and will reward the player with xp if non compostable, xp will be dropped- she will ask trivia questions about different items and where they should belong."
    super(NPC).__init__(name, location, description) """


class Winstell():
        name = "Winstell"
        location = "Recylcing Center Owner"
        description = "Winstell owns a recycling center and the player can drop off recyclable trash or else, xp will drop."
        super(NPC).__init__( name, location, description)


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

""" 
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
        print("Jack: Oh well, come again later.")"""

