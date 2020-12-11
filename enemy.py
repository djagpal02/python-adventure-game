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
        self.EXP_given = int(self.level*50 +150)


################################################  Enemies ##############################################################################################
class a1(enemy):
    def __init__(self,level = 1, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"




class a2(enemy):
    def __init__(self,level = 2, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"




class a3(enemy):
    def __init__(self,level = 3, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"




class b1(enemy):
    def __init__(self,level = 4, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class b2(enemy):
    def __init__(self,level = 5, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class b3(enemy):
    def __init__(self,level = 6, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class c1(enemy):
    def __init__(self,level = 7, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class c2(enemy):
    def __init__(self,level = 8, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class c3(enemy):
    def __init__(self,level = 9, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}
        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"






class d1(enemy):
    def __init__(self,level = 10, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class d2(enemy):
    def __init__(self,level = 11, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class d3(enemy):
    def __init__(self,level = 12, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}
        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"






class e1(enemy):
    def __init__(self,level = 13, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"






class e2(enemy):
    def __init__(self,level = 14, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class e3(enemy):
    def __init__(self,level = 15, items = {}):
        super().__init__(level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

        coin_toss = random()
        if coin_toss < 0.5:
            self.name = "bob"
        else:
            self.name = "bob2"





class boss(enemy):
    def __init__(self,name, level, items = {}):
        super().__init__(name, level, items)
        """
        Constructor Method
        ...
 
        :param level: character strength level - determines HP, AD, Gold, EXP_given
        :param items: Items carried by user (default = {})
        :type level: int
        :type items: list
        """
        self.items = {}

enemies = {11:a1,12:a2, 13:a3, 14:b1, 15:b2, 16:b3, 17:c1, 18:c2, 19:c3, 20:d1, 21:d2, 22:d3, 23:e1, 24:e2, 25:e3}