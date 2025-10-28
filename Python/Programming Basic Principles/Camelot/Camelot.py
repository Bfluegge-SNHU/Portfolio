import pygame
import os
from characterCreate import playerInit, focusSelection, classSelection, playerClass

#Player initialization
player = playerInit.playerInit()
os.system('cls')

#Class choice
player = classSelection.characterClass(player)
os.system('cls')

#focus choice
player = focusSelection.focusSelection(player['Class'], player)
os.system('cls')

#Final creation of player object
playerOne = playerClass.Player(
    player['name'], 
    player['inv'], 
    player['spells'], 
    player['Class'], 
    player['focus'], 
    player['Gender'], 
    player['Age'], 
    {'gold' : player['Money']['gold'], 'silver' : player['Money']['silver'], 'copper' : player['Money']['copper']}
    )

os.system('cls')
print(playerOne.name + " The " + playerOne.Class + "\nFocus: " + playerOne.focus + "\n")
print("Inventory: \n" + str(playerOne.inv))
print("Gold: " + str(playerOne.Money['gold']) + " Silver: " + str(playerOne.Money['silver']) + " Copper: " + str(playerOne.Money['copper']))
print("*" * 20)
print("Spells: \n" + str(playerOne.spells))
print("*" * 20)
confirm = input("Does this information look correct? [y/n] > ")

if confirm == 'y' or confirm == 'Y' or confirm == 'yes' or confirm == 'Yes':
    print("\n\nWelcome to Camelot! \n\nHome of the knights of the round table! \n\nWhere your story has yet to unfold...\n")
    input("Press Enter to Continue...")
