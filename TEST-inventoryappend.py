from final import guess
from quests import NPC 
from Player import Player

for i in Player:
    i['Name'] = "Judy"

guess()

print(NPC.quest_Jack())