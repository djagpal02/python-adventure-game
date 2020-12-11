from Map import all_maps # for change map algorithm
from shops import all_shops # To find correct shop in shop algorithm
from bed import all_beds # To find correct bed in bed algrorithm

class location:
    """
    A class to represent the users current position in the game world

    Uses the current map along with position coordinates to find current position
    ...

    Arguments
    ---------
    :param MAP: The matrix the user is currently in
    :type MAP: MAP
    :param row: row within matrix of map
    :type row: int
    :param col: col within matrix of map
    :type col: int

    Methods
    -------
    changemap(placeholder)
        Uses doors and map keys to Jump between maps
    shop(player, placeholder)
        Uses shop key to allow player to access shops and make purchases
    bed(player,placeholder)
        Uses bed key to allow player to access beds to save game and regenerate hit points
    """



    def __init__(self, MAP, row, col):
        """
        Constructor
        ...

        Parameters
        ----------
        :param MAP: The matrix the user is currently in
        :type MAP: MAP
        :param row: row within matrix of map
        :type row: int
        :param col: col within matrix of map
        :type col: int
        """
        self.map = MAP
        self.row = row
        self.col = col



    def changemap(self, placeholder):
        """
        Uses doors and map keys to Jump between maps
        ...

        Parameters
        ----------
        :param placeholder: 2nd value of tuple from matrix map, associated with keys
        :type placeholder: str
        """
        x = self.map.key # store current map key before changing map
        for i in all_maps: # Find the map matching the door/key
            if i.key == placeholder:
                self.map = i # Once found, set current map to new map
                for vector in self.map.doors: # Check each door if it has the matching opposite door
                    r = vector[0]
                    c = vector[1]
                    if self.map.matrix[r][c][1] == x: # Once door is found enter one space to the right of the door
                        self.row = r
                        self.col = c + 1



    def shop(self,player, placeholder):
        """
        Uses shop key to allow player to access shops and make purchases
        ...

        Parameters
        ----------
        :param player: game user
        :type player: player.character
        :param placeholder: 2nd value of tuple from matrix map, associated with keys
        :type placeholder: str
        """
        for shop in all_shops: # To determine which items to display search for shop in all shops
            if shop.key == placeholder: # Once found, print list of available items
                print(f"Welcome,  we have: ")
                for i in shop.available_items:
                    print(f"{i.name} for {i.value} gold")
                x = "exit"#input("Would you like to purchase anything? if no type exit otherwise select an item") # Ask user for purchase ###TODO
                if x == "exit": # if user changes mind
                    break
                else:
                    shop.purchase(player,x) # Send to purchase algorithm



    def bed(self, player, placeholder):
        """
        Uses bed key to allow player to access beds to save game and regenerate hit points
        ...

        Parameters
        ----------
        :param player: game user
        :type player: player.character
        :param placeholder: 2nd value of tuple from matrix map, associated with keys
        :type placeholder: str
        """
        for bed in all_beds: # Determine which bed using bed keys and given key
            if bed.key == placeholder:
                x = "no" #input(f"This bed will cost {bed.cost} for the night \n Do you wish to continue? yes/no?") # User confirmation TODO
                if x.lower() == "yes": # Lowercase to avoid captil letter errors
                    bed.use_bed(player) # If user wants to use bed, send to use_bed algorithm 
                elif x.lower() == "no": # If user chooses no, allow user back to map
                    pass
                else:
                    print("Invalid input") # Any other inputs are met with this error message
