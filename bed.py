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

        # List created of all beds, so player can loop through and find correct one from map
        all_beds.append(self)



# Create beds
home_bed = bed("HOMEB")
t2_hotel_bed = bed("HTLB2",250)
t3_hotel_bed = bed("HTLB3",1000)
t4_hotel_bed = bed("HTLB4",2000)