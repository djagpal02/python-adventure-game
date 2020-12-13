from player import player
from location import location # To give position to player on loading old game#
from Map import all_maps # To find current map when loading old game
from items import all_items , pot, weapon, shield, armour# To recreate items dictionary from string
from game import new_game, load_game
from textui import Textui
from gui import myApp,win,printer
import tkinter as tk

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
        st = int(f.readline())
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
    user = player(location(curr_map,cl_row,cl_col),location(curr_map,cl_row,cl_col), level,name,exp,exp_n,gold, bag,st)
    for i in non_pot_items:
        user.add_item(i)

    return user


def startgame(App):
    x = myApp.username
    print(App.gametype)
    if App.gametype.get() == 0:
        t_game = new_game(x)
    elif App.gametype.get() == 1:
        try:
            user = loadgame(x)
            t_game = load_game(user)
        except:
            print("Unable to find user data, will load a new game...")
            t_game = new_game(x)
    else:
        t_game = new_game(x)
    return t_game


def inpt():
    pass

def movement(move,textui,this_game,myApp=myApp):
    if myApp.contin == True:
        if move == "a":
            this_game.user.left()
            textui.show_map(this_game)
            myApp.show_map2(this_game)
        elif move == "w":
            this_game.user.up()
            textui.show_map(this_game)
            myApp.show_map2(this_game)        
        elif move == "s":
            this_game.user.down()
            textui.show_map(this_game)
            myApp.show_map2(this_game)
        elif move == "d":
            this_game.user.right()
            textui.show_map(this_game)
            myApp.show_map2(this_game)

def main():
    """
    Main function, includes intro and user functionality, such as movement
    """
    myApp.enter.wait_variable(myApp.num)
    this_game = startgame(myApp)

    textui = Textui()
    win.bind("<w>",lambda x:movement("w",textui,this_game))
    win.bind("<a>",lambda x:movement("a",textui,this_game))
    win.bind("<s>",lambda x:movement("s",textui,this_game))
    win.bind("<d>",lambda x:movement("d",textui,this_game))
    win.bind("<Return>",lambda x:myApp.contin_switch())

    win.mainloop()


if __name__ == "__main__":
    main()