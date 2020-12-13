from character import character
from random import random

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
        :param EXP_given: amount of experience points awarded to user if defeated
        :type level: int
        :type name: str
        :type items: list
        :type EXP_given: int
        """
        self.name = name
        self.gold = int(self.level*50*(0.75 + 0.5*random()))
        self.items = items
        self.level = level
        self.EXP_given = int(self.level*200 +150)


################################################  Enemies ##############################################################################################
def enemy_name(level):
    names = {
        1:"",
        2:"",
        3:"",
        4:"",
        5:"",
        6:"",
        7:"",
        8:"",
        9:"",
        10:"",
        11:"",
        12:"",
        13:"",
        14:"",
        15:""
    }
    return names[level]

