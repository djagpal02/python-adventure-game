from Map import all_maps
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

        Return
        ------
        :return True: TO inform method has been completed
        :type True: Bool
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

        return True