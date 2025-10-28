#Focuses are subcategories for player classes
import os

def focusSelection(Class, player):
    selected = False
    while selected == False:
        os.system('cls')
    #Ranger focuses
        if Class == "Ranger":
            focus = input("Select your focus:\n 1.) Thief\n 2.) Survivalist\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'theif', 'Theif'):
                player['focus'] = 'Thief'
                selected = True
            elif focus in ('2', 'survivalist', 'Survivalist'):
                player['focus'] = 'Survivalist'
                selected = True
            else:
                print("Incorrect Selection")
                continue
                

            

    #Barbarian focuses
        elif Class == "Barbarian":
            focusOptions = {'berserker', 'beast'}

    #Healer focuses
        elif Class.name == "Healer":
            focusOptions = {'shaman', 'druid'}

    #Mage focuses
        elif Class.name == "Mage":
            focusOptions = {'necromancer', 'wizard/witch'}

    #Paladin focuses
        elif Class.name == "Paladin":
            focusOptions = {'Crusader', 'Demonologist'}
                            
    #Incorrect selection
        else:
            print("Incorrect class")

    return player
