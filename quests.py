import json
import os
from Player import Player
from Player import stat
import random
## Open the JSON file of inventory
inventory = open("./inventory.json", encoding="utf8")
## create variable "inventory" that represents the enitre inventory list
inventory = json.load(inventory)

class NPC():
    def quest_Jack():

        print("Quest #1 - Description: Collect 3 items that are classified trash, Reward: 5 XP")
        #description
        answer = input("Do you want to check quest completion status? (Y/N) ")
        if answer.upper() == "Y":
            for i in inventory:
                if int(len(inventory)) >= 3:
                    del inventory[0]
                    del inventory[0]
                    del inventory[0]

                    # Creates a new JSON file with the updated inventory
                    new_file = "updated.json"
                    with open(new_file, "w") as f:
                        # Serialize the updated Python list to a JSON string
                        json_string = json.dumps(inventory)

                        # Write the JSON string to the new JSON file
                        f.write(json_string)

                    # Overwrite the old JSON file with the new one
                    os.remove("inventory.json")
                    os.rename(new_file, "inventory.json")

                    for i in Player:
                        i['Total_XP'] = i['Total_XP'] + 2
                        print("Jack: Congrats! You’ve successfully completed the quest -- Here’s your reward: *5 XP*")
                        stat.stat_checker()
            else:
                print("Jack: Not quite.(￣﹏￣；) Come back when you collect more items. ")
        else:
            input("Come back later!")


    def quest_Fiona():
        print("Quest #2 - Description: Collect 5 items, Reward: 10 XP")
        #description
        answer = input("Do you want to check quest status? (Y/N) ")
        if answer.upper() == "Y":
            if int(len(inventory)) >= 5:



                choose = random.randint(1,5)
                if choose == 1:
                    ans = input("Which is organic waste? (Type the letter) [A: Plastic Bottles B: Containers C: Newspaper D: Plastic Bags]:  ")
                    if ans.upper() == "C":
                        print("Fiona: Amazing! Whether it was pure luck or your knowledge, you got it right!")
                        print("Fiona: Now you will get your reward! \(￣︶￣*\))")
                        granted = True

                    else: 
                        print("Fiona: Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Fiona: Try again next time")
                        granted = False

                elif choose == 2:
                    ans = input("What do microorganisms need to survive? (Type the letter) [A: Water  B: Mr. Whalen's Class C: Takis D: Phone]: ")
                    if ans.upper() == "A":
                        print("Fiona: Amazing! Whether it was pure luck or your knowledge, you got it right!")
                        print("Fiona: Now you will get your reward! \(￣︶￣*\))")
                        granted = True

                    else: 
                        print("Fiona: Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Fiona: Try again next time")
                        granted = False
                        
                elif choose == 3:
                    ans = input("What is required for composting? (Type the letter) [A: Human care 24/7 B: Soil C: Plastic D: Candy]: ")
                    if ans.upper() == "B":
                        print("Fiona: Amazing! Whether it was pure luck or your knowledge, you got it right!")
                        print("Fiona: Now you will get your reward! \(￣︶￣*\))")
                        granted = True

                    else: 
                        print("Fiona: Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Fiona: Try again next time")
                        granted = False

                elif choose == 4:
                    ans = input("What air is added during the composting process? (Type the letter) [A: Nitrogen B: Oxygen C: Carbon dioxide D: Nuclear Gas]: ")
                    if ans.upper() == "B":
                        print("Fiona: Amazing! Whether it was pure luck or your knowledge, you got it right!")
                        print("Fiona: Now you will get your reward! \(￣︶￣*\))")
                        granted = True
                    else: 
                        print("Fiona: Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Fiona: Try again next time")
                        granted = False

                elif choose == 5:
                    ans = input("To aid decomposition, bigger pieces of organic waste need to be (Type the letter) [A: Broken Apart B: Shredded C: Stepped On D: Spit On]: ")
                    if ans.upper() == "A":
                        print("Fiona: Amazing! Whether it was pure luck or your knowledge, you got it right!")
                        print("Fiona: Now you will get your reward! \(￣︶￣*\))")
                        granted = True
                    else: 
                        print("Fiona: Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Fiona: Try again next time")
                        granted = False


                del inventory[0]
                del inventory[0]
                del inventory[0]
                del inventory[0]
                del inventory[0]

                # Creates a new JSON file with the updated inventory
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    # Serialize the updated Python list to a JSON string
                    json_string = json.dumps(inventory)

                    # Write the JSON string to the new JSON file
                    f.write(json_string)

                # Overwrite the old JSON file with the new one
                os.remove("inventory.json")
                os.rename(new_file, "inventory.json")

                if granted == True:
                    for i in Player:
                        i['Total_XP'] = i['Total_XP'] + 10
                        print("Fiona: Nice! This is your reward: *+10 XP*")
                        stat.stat_checker()

                elif granted == False:
                    print("Fiona: Since you answered the trivia incorrectly, you loose five items and dont't get a reward. ")
            else:
                print("Fiona: Sorry, you don't have enough items. Come back when you collect more items. ")
        else:
            input("Fiona: Alright, come back when you ready.")

    def quests_Winstell():
        print("Description: Collect 8 items, Reward: 20 XP") 
        #description
        answer = input("Do you want to check quest status? (Y/N) ")
        if answer.upper() == "Y":
            if int(len(inventory)) >= 8:
                del inventory[0]
                del inventory[0]
                del inventory[0]
                del inventory[0]
                del inventory[0]
                del inventory[0]
                del inventory[0]
                del inventory[0]
                
                # Creates a new JSON file with the updated inventory
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    # Serialize the updated Python list to a JSON string
                    json_string = json.dumps(inventory)

                    # Write the JSON string to the new JSON file
                    f.write(json_string)

                # Overwrite the old JSON file with the new one
                os.remove("inventory.json")
                os.rename(new_file, "inventory.json")


                if granted == True:
                    for i in Player:
                        i['Total_XP'] = i['Total_XP'] + 10
                        print("Winstell: Nice! This is your reward: *+10 XP*")
                        stat.stat_checker()

                elif granted == False:
                    print("Winstell: Since you answered the trivia incorrectly, you loose five items and dont't get a reward. ")

            else:
                print("Winstell: You haven't completed the quest yet. Come back when you collect more items. ")
        else:
            input("Winstell: No worries, come back when you're ready")



    def trivia_winstell():
        choose = random.randint(1,5)
        if choose == 1:
            ans = input(" ")
            if ans.upper() == "":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                print("Try again next time")
        elif choose == 2:
            ans = input(" ")
            if ans.upper() == "":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                print("Try again next time")
        elif choose == 3:
            ans = input(" ")
            if ans.upper() == "":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                print("Try again next time")
        elif choose == 4:
            ans = input(" ")
            if ans.upper() == "":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；)")
                print("Try again next time")

NPC.quest_Jack()