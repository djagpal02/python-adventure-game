from player import player

class game:
    """
    A class to represent a game, for one user]
    ...

    Arguments
    ---------
    :param name: Name of user
    :type name: str
    :param user: the useres ingame character
    :type user: player.character
    """
    def __init__(self,name, user):
        """
        Constructor
        ...

        Parameters
        ----------
        :param name: Name of user
        :type name: str
        :param user: the useres ingame character
        :type user: player.character
        """
        self.name = name
        self.user = user



    def showMap(self):
        """
        Function that prints a map to console with location of the user
        """
        overall_matrix = []
        for i in self.user.current_location.map.matrix:
            inner_lists = []
            for j in i:
                inner_lists.append(j[1])
            overall_matrix.append(inner_lists)
            
        temp = overall_matrix
        y = self.user.current_location.row
        x = self.user.current_location.col
        temp_var = temp[y][x]
        temp[y][x] = "PLYER" 
        for i in temp:
            print(i)
        temp[y][x] = temp_var
    

    def show_map(self):
        try: 
            self.showMap()
        except IndexError:
            print("hi")

    def menu(self):
        """
        A function that prints a list of options for the user
        """
        print("Please pick from the list [a, w, s, d, stats]")





class new_game(game):
    """
    A class to intiate a new game, type of game
    ...

    Arguments
    ---------
    :param name: Name of user
    :type name: str
    """
    def __init__(self,name):
        """
        Constructor
        ...

        Parameters
        ----------
        :param name: Name of user
        :type name: str
        """
        super().__init__(self,name)
        self.name = name
        self.user = player(level=1, name = self.name, EXP=0, gold= 150, items ={})




class load_game(game):
    """
    A class to load up an old game via user data
    ...

    Arguments
    ---------
    :param user: the useres ingame character
    :type user: player.character
    """
    def __init__(self,user):
        """
        Constructor
        ...
        
        Parameters
        ----------
        :param user: the useres ingame character
        :type user: player.character
        """
        super().__init__(self,user)
        self.user = user


