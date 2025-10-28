#Focuses are subcategories for player classes
def focusSelection(Class, player):
    #Ranger focuses
    if Class == "Ranger":
        focusOptions = {'Thief', 'Survivalist'}
        focus = input("Select your focus:\n 1.) Thief\n 2.) Survivalist\n")

        if focus == '1' or 'Thief' or 'thief':
            print("")
            player['focus'] = 'Thief'
        elif focus == '2' or 'Survivalist' or 'survivalist':
            player['focus'] = 'Survivalist'
                

            

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