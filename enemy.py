from character import character # base class
from random import random # For randomizing gold carried

class enemy(character):
    """
    Enemies for user to fight

    Ontop of character attributes includes EXP_given and has variable gold to allow for computer generated
    enemies.  
    ...

    Attributes
    ----------
    :param level: character strength level - determines HP, AD, gold, EXP_given
    :param name: chosen name for character (default = "No Name")
    :param items: Items carried by user (default = {})
    :param EXP_given: amount of experience points awarded to user if defeated
    :type level: int
    :type name: str
    :type items: list
    :type EXP_given: int
    """

    def __init__(self,level, name = "No Name", items = {}, EXP_given = 0):
        super().__init__(level, name, items)       
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, gold, EXP_given
        :param name: chosen name for character (default = "No Name")
        :param items: Items carried by user (default = {})
        :param gold: Amount of gold carried
        :param EXP_given: amount of experience points awarded to user if defeated
        :type level: int
        :type name: str
        :type items: list
        :type gold: int
        :type EXP_given: int
        """
        self.gold = int(self.level*50*(0.75 + 0.5*random()))
        self.EXP_given = int(self.level*200 +150)


################################################  Enemies ##############################################################################################
# Dictionary that contains names of world enemies based on enemy level
names = {
        1:"Stonetree",
        2:"Razorfoot",
        3:"Phasewings",
        4:"Mistscreamer",
        5:"Corpsebug",
        6:"Murkbody",
        7:"Moldchild",
        8:"Brinestep",
        9:"Infernobrood",
        10:"Warpclaw",
        11:"Dark Flame Baby Dragon",
        12:"Nighttalon",
        13:"Voodootooth",
        14:"Long-Horned Frost Anaconda",
        15:"Titanium Vampire Hound"}

