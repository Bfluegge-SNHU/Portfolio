import pygame
from characterCreate import playerInit, focusSelection, classSelection

#Player initialization
player = playerInit.playerInit()

#Class choice
player = classSelection.characterClass(player)

#focus choice
player = focusSelection.focusSelection(player['class'], player)


print(player)
