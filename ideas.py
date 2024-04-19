# lvl 
Player = [{'Name': [], 'XP': 0, 'LVL': [0]}]

for i in Player:
    i['Name'].clear()

    n = input("What is your name? ")
    i['Name'].append(n)
    x = int(input("Input starting XP: "))
    i['XP'] = x


    x = 18
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
