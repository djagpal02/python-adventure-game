from random import random



class character:
    """
    A class that summarizes general character attributes
    ...

    Arguments
    ----------
    :param level: character strength level - determines HP, AD
    :type level: int
    :param name: chosen name for character (default = "No Name")
    :type name: str
    :param gold: Currency used in game (default = 0)
    :type gold: int
    :param items: Items carried by user (default = {})
    :type items: list
    
    Methods
    -------
    attack(opp)
        Calculates damage dealt, varies from 75% to 125% of AD (Uniform Random) and reduces opponent HP based on damage given by self.damage, used for battle
    """



    def __init__(self, level, name = "No Name", gold = 0, items = {}):
        """
        Constructor
        ...
        
        Parameters
        ----------
        :param level: character strength level - determines HP, AD
        :type level: int
        :param name: chosen name for character (default = "No Name")
        :type name: str
        :param gold: Currency used in game (default = 0)
        :type gold: int
        :param items: Items carried by user (default = {})
        :type items: list
        """
        self.level = level
        self.HP = self.level*200 # HP increases 200 per level
        self.max_HP = self.level*200
        self.AD = self.level*25  # AD increases 25 per level
        self.name = name
        self.gold = gold
        self.items = items 



    def attack(self, opp):
        """
        Calculates damage dealt, varies from 75% to 125% of AD (Uniform Random) and reduces opponent HP based on damage given by self.damage, used for battle
        ...

        Parameters
        :param opp: opponent character
        :type opp: enemy.character
        """
        dmg = int(self.AD*(0.75 + 0.5*random())) # Randomize damage from 75% to up to 125%
        print(f"{self.name} attacks.......{opp.name} takes {dmg} damage") 
        opp.HP -= dmg
        if opp.HP < 0: # If health becomes negative, it is set to 0
            opp.HP = 0
        print(f"{self.name} has {self.HP} left and {opp.name} has {opp.HP} left")





