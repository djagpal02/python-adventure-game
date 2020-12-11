from game import new_game, load_game
from player import player # To create player profile for old returning player
from location import location # To give position to player on loading old game#
from Map import all_maps # To find current map when loading old game
from items import all_items , pot, weapon, shield, armour# To recreate items dictionary from string 

def get_items(x, q):
    """
    A function to turn 2 input lists into a dictionary

    Takes string of list of item keys and item quantities and parses through them to output lists of keys and quantities. Then loops through all_items list
    to recreate dictionary.
    ...

    Parameters
    ----------
    :param x: string input from file of keys
    :type x: str
    :param q: string input from file of quantities
    :type q: int

    Returns
    -------
    :return item_dict: dictionary of items with values set as quantities
    :type item_dict: dictionary
    """
    #### Items
    y = x[1:-2] # To get rid of \n and []
    y = y.split("'") # Create list based on '
    for i in y:
        if i == '' or ', ': # get rid of useless elements
            y.remove(i)
    items = []
    for i in y:
        for j in all_items:
            if j.key == i:
                items.append(j)
    #### quantities
    q = q[1:-2]
    q = q.split(", ")
    amm = []
    for i in q:
       i = int(i)
       amm.append(i)
    #### Dictionary
    item_dict = {}
    for i in range(len(amm)):
        item_dict[items[i]] = amm[i]

    return item_dict





def loadgame(name):
    """
    Function that reads old user data from txt file and loads old game
    ...

    Parameters
    ----------
    :param name: Name entered by user
    :type name: str
    
    Returns
    -------
    :return user: User with all attributes set to what they were at the save point of last time
    :type user: player
    """
    x = name.lower() + ".txt" # create string with name matching one used to create savegames
    with open(x, 'r') as f: # open file in read mode and parse through lines in same order as data was stored
        name = f.readline().rstrip('\n') # strip of \n
        level = int(f.readline()) # turn strings into int
        gold = int(f.readline())
        items_keys = f.readline()
        item_am = f.readline()
        cl_map = f.readline().rstrip('\n')
        cl_row = int(f.readline())
        cl_col = int(f.readline())
        exp = int(f.readline())
        exp_n = int(f.readline())
    curr_map = None # emptry var to be assigned current map
    for i in all_maps:
        if i.key == cl_map:
            curr_map = i

    non_pot_items = []        # items that are not pots
    try:
        bag = get_items(items_keys,item_am) # bag containing all items
        for i in bag:
            if i.key != "hpo" and i.key != "mpo" and i.key != "upo":# if itst not a pot then remove from bag and add via add_item method to ensure stats are updated
                non_pot_items.append(i)
        for i in non_pot_items:
            del bag[i]
    except:
        bag = {}
    user = player(location(curr_map,cl_row,cl_col),location(curr_map,cl_row,cl_col), level,name,exp,exp_n,gold, bag)
    for i in non_pot_items:
        user.add_item(i)

    return user






def main():
    """
    Main function, includes intro and user functionality, such as movement
    """
    print("Welcome to my adventure game")
    print("Would you like to start a new game or load a previous one? (load/new)")
    inp = input()
    print("What is your name?")
    name = input()
    if inp == "new":
        this_game = new_game(name)
    elif inp == "load":
        try:
            user = loadgame(name)
            user.gold += 10000 ############################################################################## TODO delete this line  ######################
            this_game = load_game(user)
        except:
            print("Unable to find user data, will load a new game...")
            this_game = new_game(name)
    else:
        print("Invalid entry, will load a new game...")
        this_game = new_game(name)
        
    print("To move around use awsd, to bring up stats, type stats and to save game sleep at any bed, at home or in a hotel")
    print("Enjoy the game!")

    game_active = True
    while game_active == True:
        move = input()
        if move == "a":
            this_game.user.left()
            this_game.show_map()
        elif move == "w":
            this_game.user.up()
            this_game.show_map()
        elif move == "s":
            this_game.user.down()
            this_game.show_map()
        elif move == "d":
            this_game.user.right()
            this_game.show_map()
        elif move == "exit":
            game_active = False
        elif move == "stats":
            this_game.user.show_stats()
        else:
            this_game.menu()

if __name__ == "__main__":
    main()