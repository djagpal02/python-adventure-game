# Create list to contain all items, for looping later
all_items = []

class item:
    """
    A class used to represent ingame items
    ...
    
    Arguments
    ---------
    :param key: Unqiue Id for item
    :type key: str
    :param name: item name
    :type name: str
    :param value: price of the item
    :type value: int
    """
    def __init__(self,key,name, value):
        """
        Constructor
        ...

        Parameters
        ----------
        :param key: Unqiue Id for item
        :type key: str
        :param name: item name
        :type name: str
        :param value: price of the item
        :type value: int
        """
        self.key = key
        self.name = name
        self.value = value

        # Create list of items for ease to loop over all items later
        all_items.append(self)

    



class weapon(item):
    """
    A class to represent weapons - AD increasing items
    ...

    Arguments
    ---------
    :param key: Unqiue Id for item
    :type key: str
    :param name: item name
    :type name: str
    :param value: price of the item
    :type value: int
    :param AD: attack damage 
    :type AD: int
    """
    def __init__(self,key,name, value,AD):
        """
        Constructor
        ...

        Parameters
        ----------
        :param key: Unqiue Id for item
        :type key: str
        :param name: item name
        :type name: str
        :param value: price of the item
        :type value: int
        :param AD: attack damage 
        :type AD: int
        """
        super().__init__(key,name, value)
        self.AD = AD





class shield(item):
    """
    A class to represent shields - HP increasing items
    ...

    Arguments
    ---------
    :param key: Unqiue Id for item
    :type key: str
    :param name: item name
    :type name: str
    :param value: price of the item
    :type value: int
    :param HP: hit points 
    :type HP: int
    """
    def __init__(self,key,name,value, HP):
        """
        Constructor
        ...

        Parameters
        ----------
        :param key: Unqiue Id for item
        :type key: str
        :param name: item name
        :type name: str
        :param value: price of the item
        :type value: int
        :param HP: hit points 
        :type HP: int
        """
        super().__init__(key,name,value)
        self.HP = HP






class armour(item):
    """
    A class to represent armour - HP increasing items
    ...

    Arguments
    ---------
    :param key: Unqiue Id for item
    :type key: str
    :param name: item name
    :type name: str
    :param value: price of the item
    :type value: int
    :param HP: hit points 
    :type HP: int
    """
    def __init__(self,key,name,value, HP):
        """
        Constructor
        ...

        Parameters
        ----------
        :param key: Unqiue Id for item
        :type key: str
        :param name: item name
        :type name: str
        :param value: price of the item
        :type value: int
        :param HP: hit points 
        :type HP: int
        """
        super().__init__(key,name,value)
        self.HP = HP





class pot(item):
    """
    A class to represent HP regen items
    ...

    Arguments
    ---------
    :param key: Unqiue Id for item
    :type key: str
    :param name: item name
    :type name: str
    :param value: price of the item
    :type value: int
    :param regen: hit points that can be regenerated 
    :type regen: int
    """
    def __init__(self,key,name,value, regen):
        """
        Constructor
        ...

        Parameters
        ----------
        :param key: Unqiue Id for item
        :type key: str
        :param name: item name
        :type name: str
        :param value: price of the item
        :type value: int
        :param regen: hit points that can be regenerated 
        :type regen: int
        """
        super().__init__(key,name,value)
        self.regen = regen



################################################################  ITEMS  #######################################################################################
# Create items

########  WEAPONS  ########

basic_sword = weapon("bsw","Basic Sword", 1000, 25)
warrior_sword = weapon("wsw","Warrior Sword", 2500, 75)
royal_blade = weapon("rbl","Royal Blade", 5000, 200)
frozen_fire_blade = weapon("ffb","FrozenFire Blade", 10000, 450)
dragon_slayer = weapon("dsb","Dragon Slayer Blade", 20000, 1500)


########  Shields  ########

basic_shield = shield("bsh","Basic Shield", 750, 50)
royal_shield = shield("rhs","Royal Shield", 2000, 250)
dragon_warrior_shield = shield("dws","Dragon Warrior Shield", 15000, 1000)


########  Armour  ########

warrior_chainmail = armour("wch","Warrior Chainmail", 2000, 250)
royal_chainmail = armour("rch","Royal Chainmail", 4500, 500)
frozen_fire_chainmail = armour("ffc","FrozenFire Chainmail", 8000, 1000)
dragonscale_armour = armour("dsa","DragonScale Armour", 50000, 3000)


########  Pots  ########

hp_pot = pot("hpo","Health Potion", 150, 75)
magic_pot = pot("mpo","Magic Potion", 600, 400)
ultimate_pot = pot("upo","Ultimate Potion", 3000, 2500)


########### Story Items ###############

earls_gold = item("egl","Earl's Gold", 0)
boat = item("bt-", "Boat",0)