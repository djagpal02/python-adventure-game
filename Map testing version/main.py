from player import player
from game import game
from textui import Textui
from gui import myApp,win,printer
from gui import warning as w
from random import random
from Map import all_maps

def startgame(App):
    """
    Function creates game object based on user input
    ...

    Parameters
    ----------
    :param App: TKinter window object that deals gui
    :type App: Tk.window

    Return
    ------
    :return t_game: game for user to start playing
    :type t_game: game object
    """
    x = App.username # Pull name data from entry field
    if App.gametype.get() == 0: # Data from radio buttons - load vs new game
        t_game = game(x,new=True)
    elif App.gametype.get() == 1:
        try:
            t_game = game(x,new=False)
        except:
            w("Unable to find user data, will load a new game...")
            t_game = game(x,new=True)
    else:
        t_game = game(x,new=True)
    return t_game

def movement(move,textui,this_game,myApp=myApp):
    """
    Controls movement based on user input from tkitner window
    ...

    Parameters
    ----------
    :param move: key selector
    :type move: str
    :param this_game: game user is playing
    :type this_game: game object
    :param myApp: interactive tkinter window
    :type myApp: Tkinter window 
    """
    if myApp.contin == True:
        if move == "a":
            this_game.user.left()
            textui.show_map(this_game)
        elif move == "w":
            this_game.user.up()
            textui.show_map(this_game)       
        elif move == "s":
            this_game.user.down()
            textui.show_map(this_game)
        elif move == "d":
            this_game.user.right()
            textui.show_map(this_game)

def remaining_maps(mps):
    """
    Finds maps not in map list
    ...

    Parameters
    ----------
    :param mps: maps already seen
    :type mps: list

    Return
    ------
    :return diff: unseen maps
    :type diff: list
    """
    lst = []
    for mp in all_maps:
        lst.append(mp.key)

    diff = []
    for mp in lst:
        if mp not in mps:
            diff.append(mp)
    
    return diff


def main():
    """
    Main function, includes intro and user functionality, such as movement
    """
    this_game = game("test",new=False) # start game 
    textui = Textui()
    in_play = True
    maps = []
    moves = 0
    while in_play == True:
        moves += 1
        flt = random()
        if flt < 0.25:
            movement("w",textui,this_game)
        elif flt < 0.5:
            movement("a",textui,this_game)
        elif flt < 0.75:
            movement("s",textui,this_game)
        else:
            movement("d",textui,this_game)
        if this_game.user.current_location.map.key not in maps: # Adds all visited maps to maps list
            maps.append(this_game.user.current_location.map.key)
            diff = remaining_maps(maps)
            with open("maptest.txt", 'w') as f:
                f.write(f'# Maps Seen: {len(maps)} \n Maps seen: {maps} \n Maps Unseen: {diff} \n Moves: {moves}')
        if len(maps) == 29:
            print("All accessible - all maps reached") # once all have been visited quits program
            quit()
        

    win.mainloop()


if __name__ == "__main__":
    main()