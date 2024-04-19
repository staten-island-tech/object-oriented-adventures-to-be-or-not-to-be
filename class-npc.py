class quests():
    jacks_quests = [{'Description': "Collect 3 items",
                     'Reward': "5 XP"}
                    {'Description': "Collect 5 items",
                      'Reward': "10 XP"}
                    {'Description': "Collect 10 items ",
                     'Reward': "20 XP"}
                        ] 
    #change to functions that correspond to the requirement and reward given

    def jack_quest1(): #First quest for jack
        description = ("[Quest: Collect 3 items — Reward = 5 XP]")
        return description

class npc_Jack():
    def dialogue_1():
        player_answer = input("Hey, I’m Jack the shopkeeper! Have you come for a quest? (Y/N)").upper()
        if player_answer == "Y":
            print()
    def quests():


"""If player has (insert recyclable items):  
recycle_playeritems == true
Count the number of items (n), convert into xp (n),
add to player xp count–  for i in player:
			e = (int(i[‘xp’  
	xp= int(e + x)])
	i[‘xp’] =  new_xp
If compost_playeritems==true:
	print(f“Winstell: Great! You have recycled {n} items and gained {n} exp. Now you have {new_score}in total”
Elif compost_playeritems==false:
	print(f“Winstell: Whoops, you don’t have anything to compost. Collect some and return back here) """



class npc_Fiona():
    def dialogue_1():


class npc_Winstell():
    def dialogue_1():
        print("Winstell: “Hello, I’m Winstell. If you’ve come to recycle, you arrived at the right place! Enter (A) if you would like to recycle items in your inventory, (B) to know more on items you can recycle, or (N) to cancel?")




print(quests.jack_quest1())