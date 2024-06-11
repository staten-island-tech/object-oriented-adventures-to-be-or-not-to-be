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

        print("Quest #1 - Description: Collect 3 items that are classified trash, Reward: 2 XP")
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
                        print("Jack: Congrats! You’ve successfully completed the quest -- Here’s your reward: *2 XP*")
                    
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

            
                

            
                
        else:
            location = int(input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " ))
            


    def quest_Fiona():
        print("Quest - Description: Collect 5 items, Reward: 10 XP")
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
                        print("Fiona: Amazing! Whether it was pure luck or yo;ur knowledge, you got it right!")
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

                new_file = "updated.json"
                with open(new_file, "w") as f:
                    json_string = json.dumps(inventory)
                    f.write(json_string)
                os.remove("inventory.json")
                os.rename(new_file, "inventory.json")

                if granted == True:
                    for i in Player:
                        i['Total_XP'] = i['Total_XP'] + 10
                        print("Fiona: Nice! This is your reward: *+10 XP*")

                elif granted == False:
                    print("Fiona: Since you answered the trivia incorrectly, you loose five items and dont't get a reward. ")
            if int(len(inventory)) < 5:
                print("Fiona: Sorry, you don't have enough items. Come back when you collect more items. ")
                

            
            location = int(input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " ))

    def quests_Winstell():
        print("Quest Description: Collect 8 items, Reward: 20 XP") 
        #description
        answer = input("Do you want to check quest status? (Y/N) ")
        if answer.upper() == "Y":
            if int(len(inventory)) >= 8:

                choose = random.randint(1,6)
                if choose == 1:
                    ans = input("Is Aluminum Foil recyclable? (Type the letter) [A.Yes B.No]: ")
                    if ans.upper() == "A":
                        print("Winstell: Brilliant! Whether or not it was pure luck or your knowledge, got the right choice!")
                        print("Winstell: Now you will get your reward! d(▀̿Ĺ̯▀̿ ̿)")
                        granted = True

                    else: 
                        print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Try again next time")
                        granted = False
                        
                elif choose == 2:
                    ans = input("How much trash do Americans create each year? (Type the letter) [A: 100 million tons B.210 million tons C: 500 million tons D: none]: ")
                    if ans.upper() == "B":
                        print("Winstell: Brilliant! Whether or not it was pure luck or your knowledge, got the right choice!")
                        print("Winstell: Now you will get your reward! d(▀̿Ĺ̯▀̿ ̿)")
                        granted = True

                    else: 
                        print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Try again next time")
                        granted = False
                elif choose == 3:
                    ans = input("Where does most of the garbage go? (Type the letter) [A: To Landfills B: To your mom’s house C: To Recycling D: To composting]: ")
                    if ans.upper() == "A":
                        print("Winstell: Brilliant! Whether or not it was pure luck or your knowledge, got the right choice!")
                        print("Winstell: Now you will get your reward! d(▀̿Ĺ̯▀̿ ̿)")
                        granted = True

                    else: 
                        print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                        print("Try again next time")
                        granted = False
                elif choose == 4:
                    ans = input("The term reduce in the three important R’s (reuse,reduce, and recycle) means: (Type the letter) [A:Use something over and over again. B: Use less of something, creating smaller amounts of waste C: Make something into something new.D: Make something ugly into something beautiful.]: ")
                    if ans.upper() == "B":
                        print("Winstell: Brilliant! Whether or not it was pure luck or your knowledge, got the right choice!")
                        print("Winstell: Now you will get your reward! d(▀̿Ĺ̯▀̿ ̿)")
                        granted = True
                    else: 
                        print("Sorry, that is not the correct answer choice. (￣﹏￣；)")
                        print("Try again next time")
                        granted = False

                elif choose == 5:
                    ans = input("Approximately what percent of trash thrown away today could be recycled? (Type the letter) [A. 20 B:23 C: 40 D: 57]: ")
                    if ans.upper() == "C":
                        print("Winstell: Brilliant! Whether or not it was pure luck or your knowledge, got the right choice!")
                        print("Winstell: Now you will get your reward! d(▀̿Ĺ̯▀̿ ̿)")
                        granted = True
                    else: 
                        print("Sorry, that is not the correct answer choice. (￣﹏￣；)")
                        print("Try again next time")
                        granted = False

                elif choose == 6:
                    ans = input("Recycling 1 ton of paper saves ____ mature trees. (Type the letter) [A: 10 B: 12 C: 3 D : 17]: ")
                    if ans.upper() == "D":
                        print("Winstell: Brilliant! Whether or not it was pure luck or your knowledge, got the right choice!")
                        print("Winstell: Now you will get your reward! d(▀̿Ĺ̯▀̿ ̿)")
                        granted = True

                    else: 
                        print("Sorry, that is not the correct answer choice. (￣﹏￣；)")
                        print("Try again next time")
                        granted = False

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
                        i['Total_XP'] = i['Total_XP'] + 17


                elif granted == False:
                    print("Winstell: Since you answered the trivia incorrectly, you loose five items and dont't get a reward. ")

            if int(len(inventory)) < 8:
                print("Winstell: You haven't completed the quest yet. Come back when you collect more items. ")
                
            
        else:
            location = int(input("You have 6 available locations to go to. Type the number of one of the following: 1.) Jack's shop, 2.Fiona's flower shop, 3.) Winstell's recycling center, 4.) Park, 5.) Beach, 6.) House, 7.Trash can, 8.Check stats: " ))


    def trivia_winstell():
        choose = random.randint(1,5)
        if choose == 1:
            ans = input("Is Aluminum Foil recyclable? (Type the letter) [A.Yes B.No]: ")
            if ans.upper() == "A":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                print("Try again next time")
        elif choose == 2:
            ans = input("How much trash do Americans create each year? (Type the letter) [A: 100 million tons B.210 million tons C: 500 million tons D: none]:")
            if ans.upper() == "B":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                print("Try again next time")
        elif choose == 3:
            ans = input("Where does most of the garbage go? (Type the letter) [A: To Landfills B: To your mom’s house C: To Recycling D: To composting]: ")
            if ans.upper() == "A":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；) ")
                print("Try again next time")
        elif choose == 4:
            ans = input("The term reduce in the three important R’s (reuse,reduce, and recycle) means: (Type the letter) [A:Use something over and over again. B: Use less of something, creating smaller amounts of waste C: Make something into something new.D: Make something ugly into something beautiful.]: ")
            if ans.upper() == "B":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")
            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；)")
                print("Try again next time")

        elif choose == 5:
            ans = input("Approximately what percent of trash thrown away today could be recycled? (Type the letter) [A. 20 B:23 C: 40 D: 57]: ")
            if ans.upper() == "C":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")
            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；)")
                print("Try again next time")

        elif choose == 6:
            ans = input("Recycling 1 ton of paper saves ____ mature trees. (Type the letter) [A: 10 B: 12 C: 3 D : 17]: ")
            if ans.upper() == "D":
                print("Amazing! Whether it was pure luck or your knowledge, you got it right!")
                print("Now you will get your reward! \(￣︶￣*\))")

            else: 
                print("Sorry, that is not the correct answer choice. (￣﹏￣；)")
                print("Try again next time")

