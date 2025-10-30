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
#Each focus has it's own abilities that are scalable for each ability level
def focusSelection(Class, player):
    selected = False
    while selected == False:
        os.system('cls')

#Ranger focuses
        if Class == "Ranger":
            focus = input("Select your focus:\n 1.) Thief\n 2.) Survivalist\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'theif', 'Theif'):
                player.focus = 'Thief'
                player.spells = {'spell1' : {'name' : 'Sneak',
                                            'desc' : 'Hide yourself in the shadows',
                                            'dam' : player.stats['Dexterity'],
                                            'level' : 1,
                                            }, 
                                'spell2' : {'name' : 'Pickpocket',
                                            'desc' : 'Pull riches from your victims',
                                            'dam' : player.stats['Dexterity'] / 10,
                                            'level' : 1,
                                            }
                                }
                selected = True
            elif focus in ('2', 'survivalist', 'Survivalist'):
                player.focus = 'Survivalist'
                player.spells = {'spell1' : {'name' : 'Forage',
                                             'desc' : 'Hunt for food and items',
                                            'dam' : player.stats['Dexterity'] / 10,
                                            'level' : 1
                                            }, 
                                'spell2' : {'name' : 'Reduce to Resources',
                                            'desc' : 'Gather resources from junk items',
                                            'dam' : player.stats['Dexterity'] / 10,
                                            'level' : 1
                                            }
                                }
                selected = True
            else:
                print("Incorrect Selection")
                continue
                

            

#Barbarian focuses
        elif Class == "Barbarian":
            focus = input("Select your focus:\n 1.) Berserker\n 2.) Beast\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'berserker', 'Berserker'):
                player.focus = 'Berserker'
                player.spells = {'spell1' : {'name' : 'Rage',
                                           'desc' : 'Your strength increases greatly!',
                                            'dam' : player.stats['Strength'] + (player.stats['Strength'] / 4),
                                            'level' : 1,
                                            'dur' : 10
                                            }, 
                                'spell2' : {'name' : 'Bloodlust',
                                            'desc' : 'Your enemies have never tasted so sweet',
                                            'dam' : player.stats['Strength'] + (player.stats['Strength'] / 5),
                                            'level' : 1,
                                            }
                                }
                selected = True
            elif focus in ('2', 'beast', 'Beast'):
                player.focus = 'Beast'
                player.spells = {'spell1' : {'name' : 'Transform',
                                            'desc' : 'Channel the beast within you',
                                            'dam' : player.stats['Strength'] + (player.stats['Strength'] / 2),
                                            'level' : 1,
                                            'dur' : 10
                                            }, 
                                'spell2' : {'name' : 'Brutality',
                                            'desc' : 'Have you ever witnessed someone fight so ferociously?',
                                            'dam' : player.stats['Strength'],
                                            'level' : 1,
                                            }
                                }
                selected = True
            else:
                print("Incorrect Selection")
                continue

#Healer focuses
        elif Class == "Healer":
            focus = input("Select your focus:\n 1.) Shaman\n 2.) Druid\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'shaman', 'Shaman'):
                player.focus = 'Shaman'
                player.spells = {'spell1' : {'name' : 'Health Drain',
                                            'desc' : 'Suck the life from your opponent',
                                            'dam' : player.stats['Intelligence'] / 4,
                                            'level' : 1
                                            }, 
                                'spell2' : {'name' : 'Fortify',
                                            'desc' : 'You increase your defense!',
                                            'dam' : player.stats['Vitality'] + (player.stats['Intelligence'] / 4),
                                            'level' : 1,
                                            'dur' : 10
                                            }
                                }
                selected = True
            elif focus in ('2', 'druid', 'Druid'):
                player.focus = 'Druid'
                player.spells = {'spell1' : {'name' : 'Healing Chant',
                                            'desc' : 'Heal you and your teamates',
                                            'dam' : player.stats['Intelligence'] / 4,
                                            'level' : 1
                                            }, 
                                'spell2' : {'name' : 'Fortify',
                                             'desc' : 'You increase your defense!',
                                             'dam' : player.stats['Vitality'] + (player.stats['Intelligence'] / 4),
                                             'level' : 1,
                                             'dur' : 10
                                            }
                                }
                selected = True
            else:
                print("Incorrect Selection")
                continue

#Mage focuses
        elif Class == "Mage":
            focus = input("Select your focus:\n 1.) Necromancer\n 2.) Wizard / Witch\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'Necromancer', 'necromancer'):
                player.focus = 'Necromancer'
                player.spells = {'spell1' : {'name' : 'Summon Zombie',
                                            'desc' : 'You pull an undead servant from the earth for battle!',
                                            'dam' : player.stats['Intelligence'] / 4,
                                            'level' : 1
                                            }, 
                                'spell2' : {'name' : 'Necrosis',
                                            'desc' : 'You curse your enemy with rot!',
                                            'dam' : player.stats['Intelligence'] / 10,
                                            'level' : 1,
                                            'dur' : 4
                                            }
                                }
                selected = True
            elif focus in ('2', 'Wizard', 'Witch', 'wizard', 'witch'):
                player.focus = 'Wizard / Witch'
                player.spells = {'spell1' : {'name' : 'Shock',
                                            'desc' : 'Zap your enemies!',
                                            'dam' : player.stats['Intelligence'] / 4,
                                            'level' : 1
                                            }, 
                                'spell2' : {'name' : 'Freeze',
                                            'desc' : 'Freeze your opponent in place!',
                                            'dam' : 0,
                                            'level' : 1,
                                            'dur' : 4
                                            }
                                }
                selected = True
            else:
                print("Incorrect Selection")
                continue

#Paladin focuses
        elif Class == "Paladin":
            focus = input("Select your focus:\n 1.) Crusader\n 2.) Demonologist\n(Enter 1 or 2 on the keyboard)\n")

            if focus in('1', 'crusader', 'Crusader'):
                player.focus = 'Crusader'
                player.spells = {'spell1' : {'name' : 'Smite',
                                            'desc' : 'You call upon the gods to release their fury onto your opponent',
                                            'dam' : player.stats['Intelligence'] / 4,
                                            'level' : 1
                                            }, 
                                'spell2' : {'name' : 'Fortify',
                                             'desc' : 'You increase your defense!',
                                             'dam' : player.stats['Vitality'] + (player.stats['Intelligence'] / 4),
                                             'level' : 1,
                                             'dur' : 10
                                            }
                                }
                selected = True
            elif focus in ('2', 'demonologist', 'Demonologist'):
                player.focus = 'Demonologist'
                player.spells = {'spell1' : {'name' : 'Smite',
                                            'desc' : 'You call upon the gods to release their fury onto your opponent',
                                            'dam' : player.stats['Intelligence'] / 4,
                                            'level' : 1
                                            }, 
                                'spell2' : {'name' : 'Rebuke',
                                            'desc' : 'Burn your opponents from the inside out!',
                                             'dam' : player.stats['Intelligence'] / 5,
                                             'level' : 1
                                            }
                                }
                selected = True
            else:
                print("Incorrect Selection")
                continue
                            
    #Incorrect selection
        else:
            print("Incorrect class")

    return player
