class Player:
    def __init__(self, ):
        self.name = ''
        self.inv = {}
        self.spells = {}
        self.focus = ''
        self.Gender = ''
        self.Age = ''
        self.Money = {'gold' : 0,
                      'silver' : 0,
                      'copper' : 0
                      }

playerOne = Player()

class Barbarian(Player):
    def __init__(self, name, inv, spells, focus, Gender, Age, Money):

        self.stats = {'Strength' : 20,
                'Dexterity' : 15,
                'Vitality' : 15,
                'Intelligence' : 10}
    
        self.weapons = {'Bow', 
                'Crossbow', 
                'Pike', 
                'Axe', 
                'GreatAxe', 
                'Mace', 
                'Pole', 
                'Dagger', 
                'Sword'
                }
        
        self.Class = 'Barbarian'
        self.name = name
        self.inv = inv
        self.spells = spells
        self.focus = focus
        self.Gender = Gender
        self.Age = Age
        self.Money = Money

        
    def interface(self):
        print(self.name + " The " + self.Class + "\nFocus: " + self.focus + "\n")
        print("Inventory: \n" + str(self.inv))
        print("Gold: " + str(self.Money['gold']) + " Silver: " + str(self.Money['silver']) + " Copper: " + str(self.Money['copper']))
        print("*" * 20)
        print("Abilities: \n" + "1.) " + str(self.spells['spell1']['name']) + " 2.) " + str(self.spells['spell2']['name']))
        print("*" * 20)


    def startingStatFormat():
        print("--------------------\n|Barbarian:\n--------------------\n| Strength:     15 |\n--------------------\n| Dexterity:    15 |\n--------------------\n| Vitality:     20 |\n--------------------\n| Intelligence: 10 |\n--------------------\n")

class Ranger(Player):
    def __init__(self, name, inv, spells, focus, Gender, Age, Money):

        self.stats = {'Strength' : 15,
                'Dexterity' : 20,
                'Vitality' : 10,
                'Intelligence' : 15}
    
        self.weapons = {'Bow', 
                'Crossbow',  
                'Dagger', 
                'Sword',
                }
        
        self.Class = 'Ranger'
        self.name = name
        self.inv = inv
        self.spells = spells
        self.focus = focus
        self.Gender = Gender
        self.Age = Age
        self.Money = Money

    def interface(self):
        print(self.name + " The " + self.Class + "\nFocus: " + self.focus + "\n")
        print("Inventory: \n" + str(self.inv))
        print("Gold: " + str(self.Money['gold']) + " Silver: " + str(self.Money['silver']) + " Copper: " + str(self.Money['copper']))
        print("*" * 20)
        print("Abilities: \n" + "1.) " + str(self.spells['spell1']['name']) + " 2.) " + str(self.spells['spell2']['name']))
        print("*" * 20)

    def startingStatFormat():
        print("--------------------\n|Ranger:\n--------------------\n| Strength:     15 |\n--------------------\n| Dexterity:    20 |\n--------------------\n| Vitality:     10 |\n--------------------\n| Intelligence: 15 |\n--------------------\n")

class Healer(Player):
    def __init__(self, name, inv, spells, focus, Gender, Age, Money):

        self.stats = {'Strength' : 10,
                'Dexterity' : 15,
                'Vitality' : 15,
                'Intelligence' : 20}
    
        self.weapons = {'Staff', 
                'wand',   
                'Sword',
                }
        
        self.Class = 'Healer'
        self.name = name
        self.inv = inv
        self.spells = spells
        self.focus = focus
        self.Gender = Gender
        self.Age = Age
        self.Money = Money

    def interface(self):
        print(self.name + " The " + self.Class + "\nFocus: " + self.focus + "\n")
        print("Inventory: \n" + str(self.inv))
        print("Gold: " + str(self.Money['gold']) + " Silver: " + str(self.Money['silver']) + " Copper: " + str(self.Money['copper']))
        print("*" * 20)
        print("Abilities: \n" + "1.) " + str(self.spells['spell1']['name']) + " 2.) " + str(self.spells['spell2']['name']))
        print("*" * 20)

    def startingStatFormat():
        print("--------------------\n|Healer:\n--------------------\n| Strength:     10 |\n--------------------\n| Dexterity:    15 |\n--------------------\n| Vitality:     15 |\n--------------------\n| Intelligence: 20 |\n--------------------\n")

class Mage(Player):
    def __init__(self, name, inv, spells, focus, Gender, Age, Money):

        self.stats = {'Strength' : 10,
                'Dexterity' : 15,
                'Vitality' : 15,
                'Intelligence' : 20}
    
        self.weapons = {'Staff', 
                'wand',   
                'Sword',
                }
        
        self.Class = 'Mage'
        self.name = name
        self.inv = inv
        self.spells = spells
        self.focus = focus
        self.Gender = Gender
        self.Age = Age
        self.Money = Money

    def interface(self):
        print(self.name + " The " + self.Class + "\nFocus: " + self.focus + "\n")
        print("Inventory: \n" + str(self.inv))
        print("Gold: " + str(self.Money['gold']) + " Silver: " + str(self.Money['silver']) + " Copper: " + str(self.Money['copper']))
        print("*" * 20)
        print("Abilities: \n" + "1.) " + str(self.spells['spell1']['name']) + " 2.) " + str(self.spells['spell2']['name']))
        print("*" * 20)

    def startingStatFormat():
        print("--------------------\n|Mage:\n--------------------\n| Strength:     10 |\n--------------------\n| Dexterity:    15 |\n--------------------\n| Vitality:     15 |\n--------------------\n| Intelligence: 20 |\n--------------------\n")

class Paladin(Player):
    def __init__(self, name, inv, spells, focus, Gender, Age, Money):

        self.stats = {'Strength' : 15,
                'Dexterity' : 10,
                'Vitality' : 15,
                'Intelligence' : 20}
    
        self.weapons = {'Bow', 
                'Crossbow', 
                'Pike', 
                'Axe', 
                'GreatAxe', 
                'Mace', 
                'Pole', 
                'Dagger', 
                'Sword'
                }
        
        self.Class = 'Paladin'
        self.name = name
        self.inv = inv
        self.spells = spells
        self.focus = focus
        self.Gender = Gender
        self.Age = Age
        self.Money = Money

    def interface(self):
        print(self.name + " The " + self.Class + "\nFocus: " + self.focus + "\n")
        print("Inventory: \n" + str(self.inv))
        print("Gold: " + str(self.Money['gold']) + " Silver: " + str(self.Money['silver']) + " Copper: " + str(self.Money['copper']))
        print("*" * 20)
        print("Abilities: \n" + "1.) " + str(self.spells['spell1']['name']) + " 2.) " + str(self.spells['spell2']['name']))
        print("*" * 20)

    def startingStatFormat():
        print("--------------------\n|Paladin:\n--------------------\n| Strength:     15 |\n--------------------\n| Dexterity:    10 |\n--------------------\n| Vitality:     15 |\n--------------------\n| Intelligence: 20 |\n--------------------\n")

                
