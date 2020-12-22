from player import player
from location import location # To give position to player on loading old game#
from Map import all_maps # To find current map when loading old game
from items import all_items# To recreate items dictionary from string

class game:
    """
    A class to represent a game
    ...

    Arguments
    ---------
    :param user: the useres ingame character
    :type user: player.character

    Methods
    -------
    get_items()
        A function to turn 2 input lists into a dictionary
    """
    def __init__(self,name,new):
        """
        Constructor

        Uses algorithm to turn string data from txt file into a player object.
        ...
        
        Parameters
        ----------
        :param name: Name of user
        :type name: str
        :param new: if the game is a new or must be loaded
        :type new: Bool
        """
        if new == True:
            self.user = player(level=1, name = name, EXP=0, gold= 150, items ={})
        else:
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
                bag = self.get_items(items_keys,item_am) # bag containing all items
                for i in bag:
                    if i.key != "hpo" and i.key != "mpo" and i.key != "upo":# if itst not a pot then remove from bag and add via add_item method to ensure stats are updated
                        non_pot_items.append(i)
                for i in non_pot_items:
                    del bag[i]
            except:
                bag = {}
            user1 = player(location(curr_map,cl_row,cl_col),location(curr_map,cl_row,cl_col), level,name,exp,exp_n,gold, bag,st)
            for i in non_pot_items:
                user1.add_item(i)

            self.user = user1

    def get_items(self,x, q):
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




