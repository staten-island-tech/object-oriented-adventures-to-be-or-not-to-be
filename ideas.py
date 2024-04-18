# lvl 
Player = [{'Name': "Judy", 'XP': 17, 'LVL': [1]}]

def calc_lvl():
    quotient = []
    for i in Player:
        print(i['XP'])
        dif = int(i['XP'])/8

        quotient.append(int(dif))

        if dif.is_integer():
            print(f"You are now lvl {dif}!")
            i['LVL'].append(dif)
            

        else:
            print(f"You are now lvl {dif}!") 
        
for i in Player:
    i['LVL'].clear()
    i['LVL'].append(3)
    print(Player)