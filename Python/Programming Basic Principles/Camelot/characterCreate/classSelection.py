
#FIXME: Add the rest of class selection functionality to mimic barbarian
#FIXME: Add check before selection to verify that's the class they actually want
#FIXME: Add stats for each class
import os

def characterClass(player):
    selected = False
    
    while selected == False:
        os.system('cls')
        Class = input("Select your class, " + player['name'] +":\n 1.)Barbarian\n 2.)Ranger\n 3.)Healer\n 4.)Mage\n 5.)Paladin\n")

        if Class == '1' or Class == 'Barbarian' or Class == 'barbarian':
            print("--------------------\n|Barbarian:\n--------------------\n| Strength:     60 |\n--------------------\n| Dexterity:    30 |\n--------------------\n| Vitality:     65 |\n--------------------\n| Intelligence: 20 |\n--------------------\n")
            selector = input("Are you sure you want to be a Barbarian [y/n]:\n")

            if selector == 'y' or selector == 'Y' or selector == 'yes' or selector == 'Yes':
                player['Class'] = 'Barbarian'
                selected = True
            else:
                continue

        elif Class == '2' or Class == 'Ranger' or Class == 'ranger':
            print("--------------------\n|Ranger:\n--------------------\n| Strength:     40 |\n--------------------\n| Dexterity:    60 |\n--------------------\n| Vitality:     45 |\n--------------------\n| Intelligence: 40 |\n--------------------\n")
            selector = input("Are you sure you want to be a Ranger [y/n]:\n")

            if selector == 'y' or selector == 'Y' or selector == 'yes' or selector == 'Yes':
                player['Class'] = 'Ranger'
                selected = True
            else:
                continue
        elif Class == '3' or Class == 'Healer' or Class == 'healer':
            player['Class'] = 'Healer'
        elif Class == '4' or Class == 'Mage' or Class == 'mage':
            player['Class'] = 'Mage'
        elif Class == '5' or Class == 'Paladin' or Class == 'paladin':
            player['Class'] = 'Paladin'
        else:
            print("Incorrect Selection")

    return player
