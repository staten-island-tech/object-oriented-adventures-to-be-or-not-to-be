Player = [{'Name': "Judy", 'XP': 17, 'LVL': [10]}]


    
for i in Player:
    print(i['XP'])
    dif = int(i['XP'])/8


    Player.append(dif)


    if dif == ["1","2","3","4","5","6","7","8"]:
        print(f"You are now lvl {dif}!")
        i['LVL'].append(dif)
           

    else:
        print(f"You are lvl",i["LVL"])
       
    for i in Player:
        i['LVL'].clear()
        i['LVL'].append(1)
        print(Player)