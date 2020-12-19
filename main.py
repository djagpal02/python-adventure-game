from player import player
from game import new_game, load_game
from textui import Textui
from gui import myApp,win,printer
from gui import warning as w

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
        t_game = new_game(x)
    elif App.gametype.get() == 1:
        try:
            t_game = load_game(x)
        except:
            w("Unable to find user data, will load a new game...")
            t_game = new_game(x)
    else:
        t_game = new_game(x)
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
    myApp.enter.wait_variable(myApp.num) # wait for user to decide what kind of game (new/load)
    this_game = startgame(myApp) # start game 

    textui = Textui()
    win.bind("<w>",lambda x:movement("w",textui,this_game))
    win.bind("<a>",lambda x:movement("a",textui,this_game))
    win.bind("<s>",lambda x:movement("s",textui,this_game))
    win.bind("<d>",lambda x:movement("d",textui,this_game))
    win.bind("<Return>",lambda x:myApp.contin_switch())

    win.mainloop()


if __name__ == "__main__":
    main()