Player = [{'Name': 'Name', 'Total_XP': 0, 'LVL': 0}]

def stat_checker():
    n = input("Do you want to see your stats? (Y/N) ")

    if n.upper() == "Y":
        print(Player)