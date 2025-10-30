from hudModules import HUD
import os

def tutorialRun(player):
    print("Welcome to Camelot!\n\nMany adventurers before you have passed through these city gates!\nYour story begins now!\nFirst, we must teach you the methods of obtaining greatness...\nStart by looking at your HUD")
    input("Press enter to continue > ")
    os.system('cls')

    HUD.displayHUD(player)
    print("This is your HUD. It displays everything you will need to interact with the world around you.\n")
    input("Press enter to continue > ")
    os.system('cls')

    print("*" * 50)
    print(player.name + " The " + player.Class + " " + player.focus + "\nAbilities : 1.)" + str(player.spells['spell1']['name']) + " 2.)" + str(player.spells['spell2']['name']))
    print("_" * 50)
    print("^^ This is your character information ^^\nAll info including Name, Class, and Focus are listed here.\nAlso, this is where your abilities and spells are stored for reference.")
    input("Press enter to continue > ")
    os.system('cls')
    
    print("*" * 50)
    print(player.name + " The " + player.Class + " " + player.focus + "\nAbilities : 1.)" + str(player.spells['spell1']['name']) + " 2.)" + str(player.spells['spell2']['name']))
    print("_" * 50)
    print("Inventory: " + str(player.inv))
    print("_" * 50)
    print("^^ This is your inventory.^^\nYou can carry up to 10 items in your bag. These items will be accessible here.")
    input("Press enter to continue > ")
    os.system('cls')

    print("*" * 50)
    print(player.name + " The " + player.Class + " " + player.focus + "\nAbilities : 1.)" + str(player.spells['spell1']['name']) + " 2.)" + str(player.spells['spell2']['name']))
    print("_" * 50)
    print("Inventory: " + str(player.inv))
    print("_" * 50)
    print(player.Money)
    print("*" * 50)
    print("^^ Finally, your money is listed here ^^\nThis is currency used at shops and Inns throughout the world")
    input("Press enter to continue > ")
