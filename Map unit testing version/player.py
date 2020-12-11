from character import character # Inheritence
from items import pot, weapon, shield, armour ,all_items # To check bag for duplicate items
from fight import fight # To enage in battle
from enemy import enemies, a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3,boss # For random battles accross map
from random import random
from location import location # To set initial location
from Map import home # To set intitial location





class player(character):
    """
    A class to represent the game user

    Central class that stores all data relevant to the main character/user
    ...

    Arguments
    ---------
    :param current_location: stores position at any time
    :type current_location: location
    :param last_save_location: stores position of last save point
    :type last_save_location: location
    :param level: character strength level - determines HP, AD
    :type level: int
    :param name: chosen name for character (default = "No Name")
    :type name: str
    :param EXP: experience points
    :type EXP: int
    :param exp_needed: number of experience points required to hit next level
    :type exp_needed: int
    :param gold: Currency used in game (default = 0)
    :type gold: int
    :param items: Items carried by user (default = {})
    :type items: dictionary

    Methods
    -------
    show_stats()
        Prints user stats to the console along with contents of user bag
    savegame()
        Creates a savegame txt 
    death()
        Resets location to last_save_location and HP to max_HP
    exp_gain()
        Adds EXP based on enemy and if EXP meets level up requirements, levels up user
    use_item()
        if item is a pot, allows user to use item
    remove_item()
        allows user to get rid of an item if desired
    add_item()
        function to add a new item to user bag
    world_map_enemies()
        controls random battles on world map
    map_enemies()
        controls all random battles on all maps
    left()
        moves user location to left or interacts with something in the left position
    right()
        moves user location to right or interacts with something in the right position
    up()
        moves user location up or interacts with something in the up position
    down()
        moves user location down or interacts with something in the down position

    """
    def __init__(self,current_location = location(home,1,1),last_save_location = location(home,1,1),level = 1, name = "No Name", EXP = 0,exp_needed=500, gold = 0, items = {}):
        """
        Constructor
        ...

        Parameters
        ----------
        :param current_location: stores position at any time
        :type current_location: location
        :param last_save_location: stores position of last save point
        :type last_save_location: location
        :param level: character strength level - determines HP, AD
        :type level: int
        :param name: chosen name for character (default = "No Name")
        :type name: str
        :param EXP: experience points
        :type EXP: int
        :param exp_needed: number of experience points required to hit next level
        :type exp_needed: int
        :param gold: Currency used in game (default = 0)
        :type gold: int
        :param items: Items carried by user (default = {})
        :type items: dictionary
        """
        super().__init__(level, name, gold, items)
        self.current_location = current_location
        self.last_save_location = last_save_location
        self.EXP = EXP
        self.exp_needed = exp_needed
        self.HP = 500 + self.level*200 # HP increases 200 per level
        self.max_HP = 500 + self.level*200
        self.AD = self.level*50  # AD increases 50 per level
    


    #########################################################  SHOW STATS  ##################################################################################
    def show_stats(self):
        """
        Prints user stats to the console along with contents of user bag
        """
        print(f"""\nName : {self.name} \nLevel: {self.level} \nAD: {self.AD} \nHP: {self.HP} \nMAX HP: {self.max_HP} \nEXP for level up: {self.exp_needed} \nGold: {self.gold}
        \n...\n\nIn your bag:\n""") #prints(user stats)
        for item in self.items.keys(): # Prints items and quantities
            print(f"{item.name} x {self.items[item]}")



    #########################################################  SAVEGAME  ####################################################################################
    def savegame(self):
        """
        Creates a savegame txt 
        """
        x = self.name.lower() + ".txt" # create var string with name of user and txt at end
        things = [] # to store item keys
        amount = [] # to store item quantities
        for i,j in self.items.items(): # Fill things and amount
            things.append(i.key)
            amount.append(j)
        with open(x, 'w') as f: # Opens file x and writes or overwrites data
            f.write(f"{self.name}\n{self.level}\n{self.gold}\n{things}\n{amount}\n{self.current_location.map.key}\n{self.current_location.row}\n{self.current_location.col}\n{self.EXP}\n{self.exp_needed}")
        self.last_save_location = location(self.current_location.map, self.current_location.row, self.current_location.col) # Changes last save location


    
    #########################################################  DEATH  ###########################################################################################
    def death(self):
        """
        Resets location to last_save_location and HP to max_HP
        """
        self.current_location = location(self.last_save_location.map, self.last_save_location.row, self.last_save_location.col) # Reset location
        self.HP = self.max_HP # Reset HP

    

    #########################################################  LEVEL UP  #####################################################################################
    def exp_gain(self, opponent):
        """
        Adds EXP based on enemy and if EXP meets level up requirements, levels up user
        ...

        Parameters
        ----------
        :param opponent: enemy that has been battled
        :type opponent: enemy.character
        """
        self.EXP += opponent.EXP_given # Add EXP
        if self.EXP > self.exp_needed: # If EXP meets requirements LEVEL UP
            self.level += 1
            self.exp_needed = int(self.exp_needed + self.exp_needed*1.1)
            print(f"{self.name} just leveled up to Level {self.level}!!")
    


    ###########################################################  ITEMS  ###################################################################################### 
    def use_item(self,x):
        """
        if item is a pot, allows user to use item
        ...

        Parameters
        ----------
        :param x: user input for selected item
        :type x: str

        Return
        ------
        :return used: if an item was actually used
        :type used: bool
        """
        list = self.items.keys() # Create list of items in bag
        used = False # To determine if an item was actually used
        temp = None
        for i in list:  # Check what item the key matches too
            if i.name.lower() == x.lower(): # lower case to avoid captial letter errors
                if type(i) == pot: # can only be used if item is a pot
                    temp = i
                    i.use(self)
                    used = True
        try:
            if self.items[temp] > 1: # if the above was successfull temp will now be assigned otherwise this will have an error and except will run
                self.items[temp] -= 1 # if pot was used the quantity must go down by 1
            else: 
                del self.items[temp] # if there only was 1 it must be deleted
        except:
            pass # allow error, just do nothing

        return used




    def remove_item(self,item):
        """
        allows user to get rid of an item if desired
        ...

        Parameters
        ----------
        :param item: item in bag
        :type item: item
         
        Return
        ------
        :return response: response based on whether function was successfull or not
        :type response: str
        """
        if item not in self.items: # If item is not in dict bag
            response = f"You do not have {item} in inventory"
        else:
            del self.items[item]
            if type(item) == weapon: # if item is of type weapon, associated ad must be removed
                self.AD -= item.AD
            elif type(item) == shield or type(item) == armour: # if item is of time shield or armour, associated HP must be removed
                self.HP -= item.HP
                self.max_HP -= item.HP
            response = f"{item} has been removed from inventory"

        return response



    def add_item(self, item):
        """
        function to add a new item to user bag
        ...

        Parameters
        ----------
        :param item: item in bag
        :type item: item
         
        Return
        ------
        :return item_added: to inform shop if a purchase was made or not
        :type item_added: bool
        """
        x = type(item) # log what the item is
        contents = []   # Log of types of items in bag
        things_list = [] # Log of items in bag
        item_added = False
        for thing in self.items.keys():
            things_list.append(thing.name.lower())
            contents.append(type(thing))
        if item.name.lower() in things_list: # if item is already in bag
            if x == pot: # if it is a pot then player can have more than 1 otherwise is limited
                self.items[item] += 1
                item_added = True
                print(f"You now have another {item.name}")
            elif x == weapon or x == shield or x == armour:
                print("You already have one")
        else: # If it is not already in bag
            if x == pot: # New pot 
                self.items[item] = 1
                item_added = True
                print(f"{item.name} has been added to your inventory")
            else:
                if x in contents: # if it is not a pot then matching types cannot be bough until an old one is gotten rid off
                    print(f"Please get rid of your old weapon/shield/armour before purchasing a new one")
                    removal = input("Would you like to get rid of an item? (yes/no)") # Allow user to delete old item
                    if removal.lower() == "yes":
                        self.show_stats() # Show items for user 
                        to_be_removed = input("What item would you like removed? (Enter name)") # Find item to be deleted
                        for i in all_items:
                            if i.name.lower() == to_be_removed.lower():
                                self.remove_item(i)
                                print("Item was removed") # If it was removed then this message will display
                else:
                    self.items[item] = 1 # If it is not in bag or same type isnt in bag, simply add 1 unit to bag
                    item_added = True
                    if type(item) == weapon:
                        self.AD += item.AD # scale Ad based on items
                    elif type(item) == shield or type(item) == armour:
                        self.HP += item.HP # Scale hp based on items
                        self.max_HP += item.HP
                    print(f"{item.name} has been added to your inventory")
        
        return item_added



    
    ########################################################################  RANDOM FIGHTS  ###############################################################
    def world_map_enemies(self, a,b,c):
        """
        controls random battles on world map
        ...

        Parameters
        ----------
        :param a: most common enemy
        :type a: enemy.character
        :param b: common enemy
        :type b: enemy.character
        :param c: least common enemy
        :type c: enemy.character
        """
        rand_flt = random() # Generate a random uniform float number between 0 and 1 
        if rand_flt < 0.7: # 70% probability of occurance
            opponent = a()
            this_fight = fight() # Create fight object
            this_fight.full_battle(self, opponent) # engage in battle
        elif rand_flt > 0.7 and rand_flt < 0.95: # 25% probability of occurance
            opponent = b()
            this_fight = fight()
            this_fight.full_battle(self, opponent)
        else: #5% probability of occurance
            opponent = c()
            this_fight = fight()
            this_fight.full_battle(self, opponent)

            



    def map_enemies(self, val):   
        """
        controls all random battles on all maps
        ...

        Parameters
        ----------
        :param val: numeric element from map matrix, decides possible interactions
        :type val: int
        """
        flt = random() # Random number to decide how often a random battle should occur
        if flt < 0:
            if val == 26: # Set regions have varying levels of difficulty in terms of enemies
                self.world_map_enemies(a1,a2,a3)
            elif val == 27:
                self.world_map_enemies(b1,b2,b3)
            elif val == 28:
                self.world_map_enemies(c1,c2,c3)
            elif val == 29:
                self.world_map_enemies(d1,d2,d3)
            elif val == 30:
                self.world_map_enemies(e1,e2,e3)
            else: # If battle is not on world map then use enemies dict. to find right strength enemy
                for num,opp in enemies.items():
                    if val == num:
                        opponent = opp()
                        this_fight = fight()
                        this_fight.full_battle(self, opponent)



    #########################################################  MOVEMENT  #############################################################################
    def left(self):
        """
        moves user location to left or interacts with something in the left position
        """
        val = self.current_location.map.matrix[self.current_location.row][self.current_location.col-1][0] # Stores numeric element of tuple
        placeholder = self.current_location.map.matrix[self.current_location.row][self.current_location.col-1][1] # stores key element of tuple
        if val < 31: # for battles and general movement
            self.map_enemies(val)
            self.current_location.col -= 1
        elif val == 50: # To enter a door to another map
            self.current_location.changemap(placeholder)
        elif val == 40: # To interact with a shop
            self.current_location.shop(self,placeholder)
        elif val == 90: # To interact with a bed
            self.current_location.bed(self,placeholder)
           



    def right(self):
        """
        moves user location to right or interacts with something in the right position
        """
        val = self.current_location.map.matrix[self.current_location.row][self.current_location.col+1][0]
        placeholder = self.current_location.map.matrix[self.current_location.row][self.current_location.col+1][1]
        if val < 31:
            self.map_enemies(val)
            self.current_location.col += 1
        elif val == 50:
            self.current_location.changemap(placeholder)
        elif val == 40:
            self.current_location.shop(self,placeholder)
        elif val == 90:
            self.current_location.bed(self,placeholder)
          


    def up(self):
        """
        moves user location up or interacts with something in the up position
        """
        val = self.current_location.map.matrix[self.current_location.row - 1][self.current_location.col][0]
        placeholder = self.current_location.map.matrix[self.current_location.row - 1][self.current_location.col][1]
        if val < 31:
            self.map_enemies(val)
            self.current_location.row -= 1
        elif val == 50:
            self.current_location.changemap(placeholder)
        elif val == 40:
            self.current_location.shop(self,placeholder)
        elif val == 90:
            self.current_location.bed(self,placeholder)
          


    def down(self):
        """
        moves user location down or interacts with something in the down position
        """
        val = self.current_location.map.matrix[self.current_location.row + 1][self.current_location.col][0]
        placeholder = self.current_location.map.matrix[self.current_location.row + 1][self.current_location.col][1]
        if val < 31:
            self.map_enemies(val)
            self.current_location.row += 1
        elif val == 50:
            self.current_location.changemap(placeholder)
        elif val == 40:
            self.current_location.shop(self,placeholder)
        elif val == 90:
            self.current_location.bed(self,placeholder)
          