import os 
from characterCreate import classClasses

playerOne = classClasses.playerOne

def playerInit():

    #common user info gathering.
    userName = input("What is your Name?\n")
    playerOne.name = userName
    userGender = input("What is your gender, " + userName + "?\n")
    playerOne.Gender = userGender
    userAge = input("How old are you " + userName + "?\n (Note: Players must be at least thirteen years old!)\n")
    playerOne.Age = userAge

#Age limit is 13 check
    if userAge >= "13":
        print("Welcome to Camelot! Let's design your character!")
    else:
        print("Sorry you are too young for this game!\n")
        os._exit(0)
        

    return playerOne

#Class Creation Assigns a subclass of whatever class selection is made to the player
def characterClass(player):
    selected = False
#While loop to allow for selection
    while selected == False:
        os.system('cls')
        Class = input("Select your class, " + player.name +":\n 1.)Barbarian\n 2.)Ranger\n 3.)Healer\n 4.)Mage\n 5.)Paladin\n")

#Barabarian selection
        if Class == '1' or Class == 'Barbarian' or Class == 'barbarian':
            print(classClasses.Barbarian.startingStatFormat())
            selector = input("Are you sure you want to be a Barbarian [y/n]:\n")

            if selector == 'y' or selector == 'Y' or selector == 'yes' or selector == 'Yes':
                playerOne = classClasses.Barbarian(player.name, player.inv, player.spells, player.focus, player.Gender, player.Age, player.Money)
                selected = True
            else:
                continue

#Ranger selection
        elif Class == '2' or Class == 'Ranger' or Class == 'ranger':
            print(classClasses.Ranger.startingStatFormat())
            selector = input("Are you sure you want to be a Ranger [y/n]:\n")

            if selector == 'y' or selector == 'Y' or selector == 'yes' or selector == 'Yes':
                playerOne = classClasses.Ranger(player.name, player.inv, player.spells, player.focus, player.Gender, player.Age, player.Money)
                selected = True
            else:
                continue

#Healer selection
        elif Class == '3' or Class == 'Healer' or Class == 'healer':
            print(classClasses.Healer.startingStatFormat())
            selector = input("Are you sure you want to be a Healer [y/n]:\n")

            if selector == 'y' or selector == 'Y' or selector == 'yes' or selector == 'Yes':
                playerOne = classClasses.Healer(player.name, player.inv, player.spells, player.focus, player.Gender, player.Age, player.Money)
                selected = True
            else:
                continue

#Mage selection
        elif Class == '4' or Class == 'Mage' or Class == 'mage':
            print(classClasses.Mage.startingStatFormat())
            selector = input("Are you sure you want to be a Mage [y/n]:\n")

            if selector == 'y' or selector == 'Y' or selector == 'yes' or selector == 'Yes':
                playerOne = classClasses.Mage(player.name, player.inv, player.spells, player.focus, player.Gender, player.Age, player.Money)
                selected = True
            else:
                continue

#Paladin selection
        elif Class == '5' or Class == 'Paladin' or Class == 'paladin':
            print(classClasses.Paladin.startingStatFormat())
            selector = input("Are you sure you want to be a Paladin [y/n]:\n")

            if selector == 'y' or selector == 'Y' or selector == 'yes' or selector == 'Yes':
                playerOne = classClasses.Paladin(player.name, player.inv, player.spells, player.focus, player.Gender, player.Age, player.Money)
                selected = True
            else:
                continue

        else:
            print("Incorrect Selection")

    return playerOne


#Focuses are subcategories for player classes
def focusSelection(Class, player):
    selected = False
    while selected == False:
        os.system('cls')

#Ranger focuses
        if Class == "Ranger":
            focus = input("Select your focus:\n 1.) Thief\n 2.) Survivalist\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'theif', 'Theif'):
                player.focus = 'Thief'
                player.spells = {'Sneak', 'Pickpocket'}
                selected = True
            elif focus in ('2', 'survivalist', 'Survivalist'):
                player.focus = 'Survivalist'
                player.spells = {'Forage', 'Reduce to Resources'}
                selected = True
            else:
                print("Incorrect Selection")
                continue
                

            

#Barbarian focuses
        elif Class == "Barbarian":
            focus = input("Select your focus:\n 1.) Berserker\n 2.) Beast\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'berserker', 'Berserker'):
                player.focus = 'Berserker'
                player.spells = {'Rage', 'Bloodlust'}
                selected = True
            elif focus in ('2', 'beast', 'Beast'):
                player.focus = 'Beast'
                player.spells = {'Transform', 'Brutality'}
                selected = True
            else:
                print("Incorrect Selection")
                continue

#Healer focuses
        elif Class == "Healer":
            focus = input("Select your focus:\n 1.) Shaman\n 2.) Druid\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'shaman', 'Shaman'):
                player.focus = 'Shaman'
                player.spells = {'Fortify', 'Healing Chant'}
                selected = True
            elif focus in ('2', 'druid', 'Druid'):
                player.focus = 'Druid'
                player.spells = {'Fortify', 'Healing Chant'}
                selected = True
            else:
                print("Incorrect Selection")
                continue

#Mage focuses
        elif Class == "Mage":
            focus = input("Select your focus:\n 1.) Necromancer\n 2.) Wizard / Witch\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'Necromancer', 'necromancer'):
                player.focus = 'Necromancer'
                player.spells = {'Summon Zombie', 'Necrosis'}
                selected = True
            elif focus in ('2', 'Wizard', 'Witch', 'wizard', 'witch'):
                player.focus = 'Wizard / Witch'
                player.spells = {'Shock', 'Freeze'}
                selected = True
            else:
                print("Incorrect Selection")
                continue

#Paladin focuses
        elif Class == "Paladin":
            focus = input("Select your focus:\n 1.) Crusader\n 2.) Demonologist\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'crusader', 'Crusader'):
                player.focus = 'Crusader'
                player.spells = {'Smite', 'Fortify'}
                selected = True
            elif focus in ('2', 'demonologist', 'Demonologist'):
                player.focus = 'Demonologist'
                player.spells = {'Rebuke', 'Smite'}
                selected = True
            else:
                print("Incorrect Selection")
                continue
                            
    #Incorrect selection
        else:
            print("Incorrect class")

    return player
