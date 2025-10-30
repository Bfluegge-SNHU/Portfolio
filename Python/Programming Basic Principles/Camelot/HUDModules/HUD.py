
def displayHUD(player):
    print("*" * 50)
    print(player.name + " The " + player.Class + " " + player.focus + "\nAbilities : 1.)" + str(player.spells['spell1']['name']) + " 2.)" + str(player.spells['spell2']['name']))
    print("_" * 50)
    print("Inventory: " + str(player.inv))
    print("_" * 50)
    print(player.Money)
    print("*" * 50)
