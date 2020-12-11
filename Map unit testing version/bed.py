from gui import printer as p

all_beds = [] # Create list of all beds for later looping



class bed:
    """
    A class to represent a bed, where user can regain Hit points and save game
    ...

    Arguments
    ---------
    :param key: Unique id key
    :type key: str
    :param cost: cost in gold to sleep at this bed
    :type cost: int

    Methods
    -------
    use_bed(player)
        Given enough gold, allows user to regain Hit points and save game
    """



    def __init__(self,key,cost = 0):
        """
        Constructor
        ...

        Parameters
        ----------
        :param key: Unique id key
        :type key: str
        :param cost: cost in gold to sleep at this bed
        :type cost: int
        """
        self.key = key
        self.cost = cost

        all_beds.append(self)



    def use_bed(self,player):
        """
        Given enough gold, allows user to regain Hit points and save game
        ...

        Parameters
        ----------
        :param player: game user
        :type player: player.character
        """
        if player.gold > self.cost: # Given user has enough gold (incase of hotel)
            p(f"{self.cost} has been charged for your stay")
            player.gold -= self.cost # Deducts gold cost
            player.HP = player.max_HP # Resets HP
            player.savegame() # Saves game
            p("The game has been saved")
        else:
            p("You have insufficient gold")




# Create beds
home_bed = bed("HOMEB")
t2_hotel_bed = bed("HTLB2",250)
t3_hotel_bed = bed("HTLB3",1000)
t4_hotel_bed = bed("HTLB4",2000)