
# Brandon Fluegge
import os

# Instruction Function
def instruction():
    print(' _    _   _____  _      _     _     _')
    print('| |__| | | |-| || |    | |    \\\\  / /')
    print('|  __  | | |-| || |--- | |---  \\\\/ /')
    print('|_|  |_| |_____||_____||_____| /__/')


    print('Welcome to Holly.\nThe object of the game is to find 6 items used to defeat the demonic entity "Holly".\n1.) The polaroid picture,\n2.) Your glasses,\n3.) The journal,\n4.) The mirror,\n5.) The black box,\n6.) Your wallet.\n\nNavigate by typing "go" and a direction [north, south, east, west],\nCollect items by typing "get" and the item name.\nType "quit" to exit and "help" to display these commands.\nGood luck!')
    start = input('Press any key to continue...')

def main():
    # Room definition:
    room = {
        'storage': {'descripts': {'sto1': 'You awaken in a small cramped storage closet. How you arrived here is a mystery. There is a door to the east.', 'sto2': 'You are now in the storage closet. There is nothing here...'}, 'name': 'storage', 'doors': 'To the east', 'east': 'hallway'},
        'hallway': {'descripts': {'hal1': 'You enter into a great hall. The wallpaper is torn and the lights don\'t seem to work. It smells... peculiar in here', 'hal2': 'You are now in the hallway...'}, 'item': 'polaroid', 'item descript': '\nA picture of a young girl and her parents. Upon picking up the picture you hear a loud wail come from the door to your right...\nBest to stay out of that room for awhile... "Holly" is written on the back of the photo', 'name': 'hallway', 'west': {'west1': 'storage', 'west2': 'game room'}, 'north': 'dining room', 'south': 'foyer', 'doors': 'To the east, west, south, and north', 'east': {'east1': 'bathroom', 'east2': 'bedroom'}},
        'game room': {'descripts': {'gam1': 'Old chess boards and card tables are strewn about. \nIt looks as though this room is the only one that has been cleaned in the last decade. \nWeird...', 'gam2': 'You are now in the game room...'}, 'item': 'key', 'doors': 'To the east.', 'item descript': '\nI wonder what this key goes to?', 'name': 'game room', 'east': 'hallway'},
        'foyer': {'descripts': {'foy1': 'You find yourself in an incredibly large foyer. The front door is chained and bolted shut. \nYou\'ll need to find another way out...', 'foy2': 'You are now in the foyer...'}, 'doors': 'To the north and east.', 'item': 'glasses', 'item descript': '\nFinally found your glasses, huh? \nNot that you would willingly want to see the environment you\'re in.', 'name': 'foyer', 'east': 'living room', 'north': 'hallway'},
        'living room': {'descripts': {'liv1': 'You enter the living room. \nIt looks as though the room was once engulfed in flame. \nThere is what was once a beautiful fire place on the wall adjacent to you. \nThe coals are still hot...', 'liv2': 'You are now in the living room...'}, 'item': 'journal', 'doors': 'To the west.', 'item descript': '\nHolly\'s journal. \nThere is some very disturbing stuff in here.', 'name': 'living room', 'west': 'foyer'},
        'bathroom': {'descripts': {'bat1': 'You enter into an old bathroom. \nThe smell in here is absolutely atrocious.', 'bat2': 'You are now in the bathroom...'}, 'item': 'mirror', 'doors': 'To the west.', 'item descript': '\nA small cracked hand held mirror. \nThe handle is tarnished by age.', 'name': 'bathroom', 'west': 'hallway'},
        'basement': {'descripts': {'bas1': 'How did you get here!? You should not be here leave NOW...\nLEAVE...\nI\'M WARNING Y0U#!2$\nLEAVE N0-~W$5!\nLEA!@###@#@%$%#...\n', 'bas2': '!@#%^%#@'}, 'doors': 'To the south.', 'name': 'basement', 'south': 'kitchen'},
        'kitchen': {'descripts': {'kit1': 'You enter into a kitchen big enough to host 10 cooks. \nThe sink is full of moldy dishes and filth. \nYou swear you can hear roaches scurry from your direction upon entering.', 'kit2': 'You are now in the kitchen...'}, 'item': 'wallet', 'doors': 'to the north and west.', 'item descript': '\nYou find a wallet. \nWhile checking the wallet for ID an ear splitting headache washes over you. \nYour memories come flooding back. \nYou remember who you are.', 'name': 'kitchen', 'west': 'dining room', 'north': 'basement'},
        'dining room': {'descripts': {'din1': 'This must\'ve once been a dining room. \nThere is an old wooden table that has rotten and collapsed in on itself. \nScraps of broken plates with rotting food can be found scattered all over the floor.', 'din2': 'You are now in the dining room...'}, 'item': 'box', 'doors': 'To the south and east.', 'item descript': '\nA little black box with "Holly" etched into it. \nI bet you could trap the restless entity in here...', 'name': 'dining room', 'south': 'hallway', 'east': 'kitchen'}
    }
  
    # Variables for future use
    inventory = []
    you_are_here = room['storage']
    curr_room = room['storage']['name']
    doors = room['storage']['doors']
    user_action = ''
    h = 0
    s = 0
    k = 0
    ba = 0
    bas = 0
    g = 0
    f = 0
    l = 0
    d = 0

  #Status function
    def show_status():
        print()
        print('*'*20)
        print()
        print('Inventory : {}'.format(inventory))
        print('Current Room : {}'.format(curr_room.capitalize()))
        print('Doors in room : {}\n'.format(doors))
        print('*'*20)
        print()
      
# Loop For game
    while user_action != 'quit':
        os.system('cls')
        show_status()


        # Description generation based on if user has been in room previously or is entering room for first time:
        if curr_room == 'hallway':
            h += 1
            if h > 1:
                print(room[curr_room]['descripts']['hal2'])
            else:
                print(room[curr_room]['descripts']['hal1'])
        elif curr_room == 'storage':
            s += 1
            if s > 1:
                print(room[curr_room]['descripts']['sto2'])
            else:
                print(room[curr_room]['descripts']['sto1'])
        elif curr_room == 'game room':
            g += 1
            if g > 1:
                print(room[curr_room]['descripts']['gam2'])
            else:
                print(room[curr_room]['descripts']['gam1'])
        elif curr_room == 'dining room':
            d += 1
            if d > 1:
                print(room[curr_room]['descripts']['din2'])
            else:
                print(room[curr_room]['descripts']['din1'])
        elif curr_room == 'kitchen':
            k += 1
            if k > 1:
                print(room[curr_room]['descripts']['kit2'])
            else:
                print(room[curr_room]['descripts']['kit1'])
        elif curr_room == 'bathroom':
            ba += 1
            if ba > 1:
                print(room[curr_room]['descripts']['bat2'])
            else:
                print(room[curr_room]['descripts']['bat1'])
        elif curr_room == 'foyer':
            f += 1
            if f > 1:
                print(room[curr_room]['descripts']['foy2'])
            else:
                print(room[curr_room]['descripts']['foy1'])
        elif curr_room == 'living room':
            l += 1
            if l > 1:
                print(room[curr_room]['descripts']['liv2'])
            else:
                print(room[curr_room]['descripts']['liv1'])
        elif curr_room == 'basement':
            bas += 1
            if bas > 1:
                print(room[curr_room]['descripts']['bas2'])
            else:
                print(room[curr_room]['descripts']['bas1'])

        # Prevent KeyError for rooms without items
        try:
            item = room[curr_room]['item']
            if 'item' in you_are_here and item not in inventory:
                print('You see a {} out of the corner of your eye...'.format(room[curr_room]['item']))
        except KeyError:
            print('No item in this room')
        print()
        print('*'*20)
        print()

        # User input collection:
        main_input = input('> ').lower()
        action = main_input.split()

        # Test for single or double word for user input
        if len(action) == 1:
            if main_input == 'quit':
                print('Thanks for playing!')
                break
            elif main_input == 'help':
                instruction()
            else:
                print('Error: That is not a command.')
                instruction()

        elif len(action) == 2:
            user_action = action[0]
            user_direction = action[1]

            # Movement mechanic:
            if user_action == 'go':
                # Movement function
                directions = ['north', 'south', 'east', 'west']
                if user_direction in directions:
                    if user_direction in you_are_here:

                        if you_are_here == room['hallway'] and user_direction == 'west':
                            choice = input(
                                'There are two doors to the west. Game Room and Storage. Which shall you choose?\n> ')
                            if choice == 'game room':
                                you_are_here = room['game room']
                                curr_room = you_are_here['name']
                                doors = you_are_here['doors']
                            elif choice == 'storage':
                                you_are_here = room['storage']
                                curr_room = you_are_here['name']
                                doors = you_are_here['doors']
                        elif you_are_here == room['hallway'] and user_direction == 'east':
                            choice = input(
                                'There are two doors to the east. Bedroom and Bathroom. Which one shall you choose?\n> ')
                            if choice == 'bedroom':
                                choice2 = input(
                                    'This is the final showdown with Holly. \nYou should not enter this room unless you have gathered all of the items to defeat her. \nAre you sure you wish to enter? > ').lower()
                                if choice2 == 'yes':
                                    # End game "Cut-scene"
                                    print(
                                        '\nYou enter the bedroom slowly.\nGazing around the room you see nothing.\nThe air in here is unearthly still...\nBefore you even have a chance to think, you hear a screech from the ceiling.\nYou look up to see a young girl glaring at you. \nHer eyes black as coal and mouth extended to horrid proportions.')
                                    start = input('Press any key to continue...')
                                    if 'glasses' in inventory:
                                        print('\nThankfully you found your glasses and can see the demon before you.')
                                        start = input('Press any key to continue...')
                                        if 'polaroid' in inventory:
                                            print(
                                                '\nYou pull the picture from your inventory and identify the beast on the ceiling as the young girl in the photo.\nUpon seeing the photo in your hand Holly leaps from the ceiling and stands before you...')
                                            start = input('Press any key to continue...')
                                            if 'journal' in inventory:
                                                print(
                                                    '\nNoticing Holly\'s reaction to the photo you think about the journal you found and immediately pull it out and begin reading from it.\nHolly drops to her knees and begins screaming as you read.')
                                                start = input('Press any key to continue...')
                                                if 'mirror' in inventory:
                                                    print(
                                                        '\nAfter a brief period of reading, you hadn\'t noticed Holly rise from the floor now levitating in the air in front of you.\nYou pull the mirror from your pocket and hold it up to show her her own reflection.')
                                                    start = input('Press any key to continue...')
                                                    if 'wallet' in inventory:
                                                        print(
                                                            '\nAs Holly gazes into the mirror she weakens. \nDrifting back to the floor and silencing as she falls into a slumber')
                                                        start = input('Press any key to continue...')
                                                        if 'box' in inventory:
                                                            print(
                                                                '\nYou pull the box from your inventory and open it. \nIn doing so a flash of light is released in the room.\nThe light finally fades and you see that Holly has disappeared from her spot in the room.\nThe box bounces and shakes. \nYou hear faint screaming and clawing within.\nIt\'s best to never open that again.')
                                                            print('\nYou have won! Thanks for playing!')
                                                            start = input('Press any key to continue...')
                                                            break
                                                        else:
                                                            print(
                                                                '\nHolly lays there silent for a brief moment and you think you have won. \nHowever, you forgot one thing: \nto trap the evil soul. \nHolly springs back to her feet and devours you.\nPerhaps there was another item that could have helped you (Box).')
                                                            print('\nYou died. Game over')
                                                            start = input('Press any key to continue...')
                                                            break
                                                    else:
                                                        print(
                                                            '\nThe mirror was working!\nAs Holly gazed into it she weakens and slowly drifts back to the floor. \nShe falls silent and ends up in a deep slumber.\nYou begin to celebrate and decide you want to buy yourself a nice treat. \nSo you go on Holly\'s macbook that\'s in her bedroom and try to order a cool new camera (or whatever you\'re into.)\nYou find one that you love and reach towards your back pocket for your wallet. \nIt\'s not there.\nYou immediately die of disappointment. \nPerhaps there was another item that could help you (Wallet).')
                                                        print('\nYou died. Game over')
                                                        start = input('Press any key to continue...')
                                                        break
                                                else:
                                                    print(
                                                        '\nAfter a brief period of reading, you realize how good Holly was as an author. \nYou got so absorbed in the journal that you forgot you were battling a demon.\nYou glance up at a now bored Holly.\nShe says "Are you done yet?" and lunges at you devouring you alive.\nPerhaps there was another item that could have helped you(Mirror).')
                                                    print('\nYou died. Game over')
                                                    start = input('Press any key to continue...')
                                                    break
                                            else:
                                                print(
                                                    '\nWatching as the demon stands before you, you completely draw a blank on what you should do next. \nYou drop the polaroid in fear.\nPerhaps there was an item that could help you(Journal)\nHolly lunges at you and devours you.')
                                                print('\nYou died. Game over.')
                                                start = input('Press any key to continue...')
                                                break
                                        else:
                                            print(
                                                '\nWith your glasses firmly in place you squeal at the horror before you. \nWithout any idea who or what you are looking at you freeze in terror.\nPerhaps there was an item that could have helped you(Polaroid)\nThe beast leaps from the ceiling and devours you.')
                                            print('\nYou died. Game over.')
                                            start = input('Press any key to continue...')
                                            break
                                    else:
                                        print(
                                            '\nYou squint your eyes and realize the danger you are in far too late. \nHolly pounces from the ceiling and devours you alive.\nPerhaps there is an item that could have helped you (Glasses).')
                                        print('\nYou died. Game over.')
                                        start = input('Press any key to continue...')
                                        break
                                if choice2 == 'no':
                                    print('Wise choice. Get your affairs in order first.')
                                    start = input('Press any key to continue...')

                            elif choice == 'bathroom':
                                you_are_here = room['bathroom']
                                curr_room = you_are_here['name']
                                doors = you_are_here['doors']

                        elif you_are_here == room['kitchen'] and user_direction == 'north':
                            if 'key' in inventory:
                                print('You unlock the door with the key.')
                                start = input('Press any key to continue...')
                                you_are_here = room['basement']
                                curr_room = you_are_here['name']
                                doors = you_are_here['doors']
                            else:
                                print('This door is locked. There has to be a key somewhere')
                                start = input('Press any key to continue...')

                        else:
                            you_are_here = room[you_are_here[user_direction]]
                            curr_room = you_are_here['name']
                            doors = you_are_here['doors']

                    else:
                        print('Can’t go that way.')
                        start = input('Press any key to continue...')
                else:
                    print('That’s not a direction')
                    print('You can "go" {}'.format(directions))
                    start = input('Press any key to continue...')

            # Item collection
            elif user_action == 'get':
                # Catch faulty user input for items
                try:
                    item = room[curr_room]['item']
                    if 'item' in you_are_here and item not in inventory:
                        user_item = user_direction
                        if user_item in room[curr_room]['item']:
                            print(room[curr_room]['item descript'])
                            print('You collect the {} and add it to your inventory.'.format(room[curr_room]['item']))
                            start = input('Press any key to continue...')
                            inventory.append(item)
                            del room[curr_room]['item']
                        else:
                            print('That item is not in this room')
                            start = input('Press any key to continue...')
                except KeyError:
                    print('There is no {} here.'.format(user_direction))
                    start = input('Press any key to continue...')
            else:
                print('That is not a command. Commands are go [direction], get [item], quit, and help')
                start = input('Press any key to continue...')


instruction()
main()
