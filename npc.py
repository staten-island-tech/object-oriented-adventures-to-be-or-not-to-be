class NPC():
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description
        
    def __str__(self):
        return f"{self.description}"
    # class template for NPC
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

class Jack():
    info_Jack = NPC('Jack', 'Shop', "Jack is a shopkeeper whose shop is alway littered, he can give quests and if you complete them, a reward will be given such as xp.")
        
    def __str__(self):
        return f"{self.name}, {self.location}, {self.description}"

    def action():
        dialogue = input("Jack: Hey, I’m Jack the shopkeeper! Have you come for a quest? (Y/N) >> ")
        if dialogue.upper() == "Y":
            print(quests.quest_Jack())
        elif dialogue.upper() == "N":
            input("Returning to to main location... ")

class Fiona():
    info_fiona = NPC('Fiona', 'Flower Shop', "Fiona is only unlocked after level 1 and she owns a flower shop where you can drop off compostable things and will reward the player with xp if non compostable, xp will be dropped- she will ask trivia questions about different items and where they should belong.")
        # dialogue = input("Fiona: Welcome to my flower shop! Would you like to (a): Compost your items or (b): Accept a quest. (Type ‘N’ to return) >> ")


class Winstell():
    info_Winstell = NPC('Winstell', 'Recylcing Center Owner', 'Winstell owns a recycling center and the player can drop off recyclable trash and xp will drop.')
    # dialogue = input("Winstell: Hello, I’m Winstell. If you’ve come to recycle, you arrived at the right place! Enter (A) if you would like to recycle items in your inventory or (B) Recieve a quest. (Type 'N' to return) >> ")


input(Jack.info_Jack)
input(Fiona.info_fiona)
input(Winstell.info_Winstell)
