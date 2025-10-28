import pygame
from characterCreate import playerInit, focusSelection, classSelection

#Player initialization
player = playerInit.playerInit()

#Class choice
player = classSelection.characterClass(player)

#focus choice
player = focusSelection.focusSelection(player['class'], player)


print(player['name'] + ": " + player['class'] + "\nFocus: " + player['focus'] + "\n")
print("Inventory: \n")
print(player['inv'])
print("*" * 20)
print("Spells: \n")
print(player['spells'])
print("*" * 20)
