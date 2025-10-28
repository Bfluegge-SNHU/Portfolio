from characterCreate import characterCreate
import os

menuSelection = ''

while menuSelection != '4':
    os.system('cls')
    print("           /------|")
    print("          /       |")
    print("         /    /---|                                 |-|           _|-|_")
    print("        /    /  /----\\-\\    /--\\_/-\\_/--\\   /----\\  | |   /----\\ |-   -|")
    print("        \\    \\ |  ||  | \\  /    |   |    \\ |  ||  |_| |__|  ||  |  | |")
    print("         \\    \\_\\____/\\__\\/_____|\\_/|_____\\\\________|____|\\____/___|_|_")
    print("/--\\-----|     ____________________________________________________    \\")
    print("\\--/-----|     ________________________________________________________/")
    print("         /    /        1.) New Game")
    print("        /    /         2.) Load Game")
    print("        \\    \\         3.) Settings")
    print("         \\    \\---|    4.) Exit")
    print("          \\       |")
    print("           \\------|")

    menuSelection = input("Please select an option [1, 2, 3, or 4] > ")
    if menuSelection == '1':
        characterCreate.characterCreate()
    elif menuSelection == '2':
        input("Feature not yet available\nPress Enter to continue")
        continue
    elif menuSelection == '3':
        input("Feature not yet available\nPress Enter to continue")
        continue
    elif menuSelection == '4':
        os._exit(0)


    



