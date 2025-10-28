import os

def playerInit():

    #player dictionary for temp storage
    player = {'name' : 'none',
              'inv' : {},
              'Money' : {'gold' : 0, 'silver' : 0, 'copper' : 0},
              'spells' : {},
              'Class' : 'none',
              'focus' : 'none',
              'Gender' : 'none',
              'Age' : 'none'
    }

    #common user info gathering.
    userName = input("What is your Name?\n")
    player['name'] = userName
    userGender = input("What is your gender, " + userName + "?\n")
    player['Gender'] = userGender
    userAge = input("How old are you " + userName + "?\n (Note: Players must be at least thirteen years old!)\n")
    player['Age'] = userAge

#Age limit is 13 check
    if userAge >= "13":
        print("Welcome to Camelot! Let's design your character!")
    else:
        print("Sorry you are too young for this game!\n")
        os._exit(0)
        

    return player


#FIXME: Add the rest of class selection functionality to mimic barbarian
#FIXME: Add check before selection to verify that's the class they actually want
#FIXME: Add stats for each class
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


#Focuses are subcategories for player classes
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

class Player:
    def __init__(self, name, inv, spells, Class, focus, Gender, Age, Money):
        self.name = name
        self.inv = inv
        self.spells = spells
        self.Class = Class
        self.focus = focus
        self.Gender = Gender
        self.Age = Age
        self.Money = Money
