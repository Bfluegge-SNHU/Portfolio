import pygame
import os
from characterCreate import playerInit, classClasses



def characterCreate():
    
#Player initialization
    player = playerInit.playerInit()
    os.system('cls')

#Class choice
    player = playerInit.characterClass(player)
    os.system('cls')

#focus choice
    player = playerInit.focusSelection(player.Class, player)
    os.system('cls')

#Final creation of player object

    os.system('cls')
    player.interface()
    confirm = input("Does this information look correct? > ")

    #FIXME: Add else statement that allows changes to character options
    if confirm == 'y' or confirm == 'Y' or confirm == 'yes' or confirm == 'Yes':
        print("\n\nWelcome to Camelot! \n\nHome of the knights of the round table! \n\nWhere your story has yet to unfold...\n")
        input("Press Enter to Continue...")
        
