from gui import printer as p

def __init__(self):

    p(""""Welcome to my adventure game
    Would you like to start a new game or load a previous one? (load/new)""")
    inp = input()
    print("What is your name?")
    name = input()
    if inp == "new":
        this_game = new_game(name)
    elif inp == "load":
        try:
            user = loadgame(name)
            this_game = load_game(user)
        except:
            print("Unable to find user data, will load a new game...")
            this_game = new_game(name)
    else:
        print("Invalid entry, will load a new game...")
        this_game = new_game(name)
        
    print("To move around use awsd, to bring up stats, type stats and to save game sleep at any bed, at home or in a hotel")
    print("Enjoy the game!")