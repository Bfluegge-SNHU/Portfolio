
def playerInit():

    #player stuff
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

    if userAge >= "13":
        print("Welcome to Camelot! Let's design your character!")
    else:
        print("Sorry you are too young for this game!\n")
        

    return player
