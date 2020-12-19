# Import items so they can be stored inside the shops
from items import (basic_sword ,warrior_sword, royal_blade, frozen_fire_blade, dragon_slayer, basic_shield, royal_shield,
                   dragon_warrior_shield, warrior_chainmail, royal_chainmail, frozen_fire_chainmail, dragonscale_armour,
                   hp_pot, magic_pot, ultimate_pot )

class shop:
    """
    A class used to represent a shop
    ...

    Attributes
    ----------
    :param key: Unique id for shop
    :type key: str
    :param available_items: Items the shop sells
    :type available_items: list
    """



    def __init__(self, key, available_items = []):
        """
        Constructor 
        ...

        Parameters
        ----------
        :param key: Unique id for shop
        :type key: str
        :param available_items: Items the shop sells
        :type available_items: list
        """
        self.key = key
        self.available_items = available_items




# Create shops, assign items to each
shop1 = shop("SHOP1", available_items=[hp_pot, basic_shield, basic_sword])
shop2 = shop("SHOP2", available_items=[magic_pot, warrior_chainmail, warrior_sword])
shop3 = shop("SHOP3", available_items=[magic_pot, royal_blade, royal_chainmail, royal_shield])
shop4 = shop("SHOP4", available_items=[ultimate_pot, frozen_fire_blade, frozen_fire_chainmail])
shopm = shop("SHOPM", available_items=[ultimate_pot, dragon_slayer, dragonscale_armour, dragon_warrior_shield])

# Create list of all shops for later looping
all_shops = [shop1, shop2, shop3, shop4, shopm]