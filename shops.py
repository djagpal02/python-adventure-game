# Import items so they can be stored inside the shops
from items import (basic_sword ,warrior_sword, royal_blade, frozen_fire_blade, dragon_slayer, basic_shield, royal_shield,
                   dragon_warrior_shield, warrior_chainmail, royal_chainmail, frozen_fire_chainmail, dragonscale_armour,
                   hp_pot, magic_pot, ultimate_pot )
from gui import printer as p

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
    
    Methods
    -------
    display_items()
        Prints list of available items and price to console
    purchase(player,x)
        Matches user input to an item and attempts user purchase
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



    def display_items(self):
        """
        Prints list of available items and price to console
        """
        p("At this shop we have: ")
        stri = ""
        for item in self.available_items:
            stri += f"{item.name} for {item.value} gold"
        p(stri)



    def purchase(self,player, x):
        """
        Matches user input to an item and attempts user purchase

        Loops through all item key list to match user input to an item and if possible purchases 
        ...

        Parameters
        ----------
        :param player: users character
        :type player: player.character
        :param x: user input
        :type x: str
        """
        temp = None # Need to initiate variable outside loop, set to None for convienence
        for i in self.available_items:
            if i.name.lower() == x.lower(): # puts all letters into lowercase to avoid captial letter errors
                temp = i
        if temp != None: # If temp has been assigned a new value
            if player.gold > temp.value: # if player has enough gold
                try:
                    item_added = player.add_item(temp)
                    if item_added == True:
                        player.gold -= temp.value
                except:
                    p("You can not have more than one, sword, shield or armour") # Error from player.add_item is due to multiple of same type of item
            else:
                p("insufficient gold")
        else:
            p("Invalid input, please try again")



# Create shops, assign items to each
shop1 = shop("SHOP1", available_items=[hp_pot, basic_shield, basic_sword])
shop2 = shop("SHOP2", available_items=[magic_pot, warrior_chainmail, warrior_sword])
shop3 = shop("SHOP3", available_items=[magic_pot, royal_blade, royal_chainmail, royal_shield])
shop4 = shop("SHOP4", available_items=[ultimate_pot, frozen_fire_blade, frozen_fire_chainmail])
shopm = shop("SHOPM", available_items=[ultimate_pot, dragon_slayer, dragonscale_armour, dragon_warrior_shield])

# Create list of all shops for later looping
all_shops = [shop1, shop2, shop3, shop4, shopm]