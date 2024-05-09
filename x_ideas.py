# lvl 
Player = [{'Name': [], 'XP': 0, 'LVL': 0}]

for i in Player:
    i['Name'].clear()

    n = input("What is your name? ")
    i['Name'].append(n)
    x = int(input("Input starting XP: "))
    i['XP'] = x


def calc_lvl():
    for i in Player:
        xp = i['XP']
        dif = int(xp)/8

        i['LVL'] = dif


        if dif.is_integer():
            print(f"You are now lvl {dif}!")
            

        else:
            print(f"You are now lvl {dif}!") 

            
calc_lvl()
print(Player)


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