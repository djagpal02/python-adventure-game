from character import character # Inheritence
from items import pot, weapon, shield, armour ,all_items, boat # To check bag for duplicate items
from enemy import enemy, names# For random battles accross map
from random import random
from location import location # To set initial location
from Map import home # To set intitial location
from story_character import all_story_characters, Mom
from gui import printer as p
from shops import all_shops # To find correct shop in shop algorithm
from bed import all_beds # To find correct bed in bed algorithm
from Map import all_maps
from gui import warning as w
from gui import printer_frame5 as pf5

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
    :param story_tracker: Numeric value that represents stages in game progression
    :type story_tracker: int

    Methods
    -------
    interact()
        Logic behind interactions with "objects" on map
    battle()
        Fight between player and an opponent
    limiter(placeholder)
        Limits access based on story tracker to force progression of story in correct order
    savegame()
        Creates a savegame txt 
    death()
        Resets location to last_save_location and HP to max_HP and deducts 10% gold
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
    def __init__(self,current_location = location(home,1,1),last_save_location = location(home,1,1),level = 1, name = "No Name", EXP = 0,exp_needed=500, gold = 0, items = {}, story_tracker = 1):
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
        self.story_tracker = story_tracker #Tracks story and allows for starting game at various points in story

    ######################################################### INTERACTIONS ###############################################################
    def interact(self,typ,placeholder):
        """
        Logic behind interactions with "objects" on map
        ...

        Paramters
        ---------
        :param typ: Informs what type of object user is interacting with 
        :type typ: str
        :param palceholder: 2nd part of tuple from matrix on a map
        :type placeholder: str

        Return
        ------
        :return int: interger value based on typ to confirm completion 
        :type int: int
        """
        if typ == "storyCharacter":
            for character in all_story_characters:
                if placeholder == character.key:
                    p(f"{character.name}:") ############################************************************* fix this TODO
                    character.interact(self)
            return 0

        elif typ == "bed":
            for bed in all_beds: # Determine which bed using bed keys and given key
                if bed.key == placeholder:
                    x = p(f"This bed will cost {bed.cost} for the night \n Do you wish to continue? yes/no?",inp=True) # User confirmation
                    if x.lower() == "yes": # Lowercase to avoid captil letter errors
                        if self.gold > bed.cost: # Given user has enough gold (incase of hotel)
                            self.gold -= bed.cost # Deducts gold cost
                            self.HP = self.max_HP # Resets HP
                            self.savegame() # Saves game
                            p("The game has been saved")
                        else:
                            p("You have insufficient gold")
                    elif x.lower() == "no": # If user chooses no, allow user back to map
                        pass
                    else:
                        p("Invalid input") # Any other inputs are met with this error message
            return 1

        elif typ == "shop":
            for shop in all_shops: # To determine which items to display search for shop in all shops
                if shop.key == placeholder: # Once found, print list of available items
                    str1 = "Welcome,  we have: "
                    for i in shop.available_items:
                        str1 += f"\n{i.name} for {i.value} gold"
                    x = p(str1 + "\nWould you like to purchase anything? if no type exit otherwise select an item",inp=True) # Ask user for purchase
                    if x == "exit": # if user changes mind
                        break
                    else:
                        temp = None # Need to initiate variable outside loop, set to None for convienence
                        for i in shop.available_items:
                            if i.name.lower() == x.lower(): # puts all letters into lowercase to avoid captial letter errors
                                temp = i
                        if temp != None: # If temp has been assigned a new value
                            if self.gold > temp.value: # if player has enough gold
                                try:
                                    item_added = self.add_item(temp)
                                    if item_added == True:
                                        self.gold -= temp.value
                                except:
                                    w("You can not have more than one, sword, shield or armour") # Error from player.add_item is due to multiple of same type of item
                            else:
                                p("insufficient gold")
                        else:
                            p("Invalid input, please try again")
            return 2

    ########################################################  FIGHT  ##############################################################################################
    def battle(self, opponent):
        """
        Fight between player and an opponent
        ...

        Parameters
        ----------
        :param opponent: enemy for user to fight
        :param type: enemy.character
        """
        winner = None  # Set winner equal to None, incase player decides to run away
        w(f"{opponent.name} attacks...")
        while winner == None:   # When a new winner is set the battle is over 
            opponent.attack(self) # Since enemies suprise the player, they get to attack first
            if self.HP <= 0: # Check if somone has won 
                winner = opponent.name
                p(f"{self.name} has been defeated.")
                break
            next_move = p("What is your next move? 1 = attack, 2 = use item , 3 = try to run ",inp = True)
            if next_move == "1": # If user chooses to retaliate
                self.attack(opponent)
                if opponent.HP <= 0: # Check if somone has won
                    winner = self.name
                    p(f"{opponent.name} has been defeated.")
            elif next_move == "2": # If user chooses to use an item
                item_selected = False # To ensure an item is actually selected and to loop around if it is not
                while item_selected == False:
                    # Item selection or exit
                    x = p("Which item would you like to use? type exit to return to battle ",inp=True)
                    if x == "exit":
                        item_selected = True
                    else:
                        outcome = self.use_item(x)
                        if outcome == True:
                            item_selected = True
                            w(f"{x} was used")
                        else:
                            w("Invalid Input")
            elif next_move == "3": # If user chooses to try and run away
                value = random() # Generate float between 0 and 1
                if value > 0.75: # To make it a 25% chance of success
                    p("You got away")
                    winner = "No winner"
                else:
                    p("You got blocked")
            else: # If entry was invalid
                w("Invalid entry, while you were choosing your were attacked....")

        if self.name == winner: # If user has won
            for i in opponent.items:
                self.add_item(i)
            self.gold += opponent.gold # Steal enemies gold
            self.exp_gain(opponent) # Gain experinece points
            p(f"{self.name} wins..... {self.name} loot {opponent.gold} and {opponent.items}")
        elif opponent.name == winner: # If user has been killed
            p("You will be taken to your last save location")
            self.death()
        
        # To clear frame5
        pf5("",0)
        pf5("",1)
        return winner





    ######################################################## LEVEL BASED MAP LIMITER ############################################################
    def limiter(self,placeholder):
        """
        Limits access based on story tracker to force progression of story in correct order
        ...

        Parameters
        ----------
        :param placeholder: key of a map
        :type placeholder: str
        """
        x = self.story_tracker

        if x < 4 and placeholder in ['2TOWN','TOWER','3TOWN','4TOWN','2CAVE']:
            p("You cannot go here yet...")
        elif x < 7 and placeholder in ['3TOWN','4TOWN','2CAVE']:
            p("You cannot go here yet...")
        elif x < 8 and placeholder in ['4TOWN','2CAVE']:
            p("You cannot go here yet...")
        else:
            self.current_location.changemap(placeholder)


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
            f.write(f"{self.name}\n{self.level}\n{self.gold}\n{things}\n{amount}\n{self.current_location.map.key}\n{self.current_location.row}\n{self.current_location.col}\n{self.EXP}\n{self.exp_needed}\n{self.story_tracker}")
        self.last_save_location = location(self.current_location.map, self.current_location.row, self.current_location.col) # Changes last save location


    
    #########################################################  DEATH  ###########################################################################################
    def death(self):
        """
        Resets location to last_save_location and HP to max_HP and deducts 10% gold
        """
        self.current_location = location(self.last_save_location.map, self.last_save_location.row, self.last_save_location.col) # Reset location
        self.HP = self.max_HP # Reset HP
        self.gold = int(self.gold*0.9)  # Lose 10% gold each time you die

    

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
            self.exp_needed = int(self.exp_needed + 500*(1.1**self.level))
            w(f"{self.name} just leveled up to Level {self.level}!!")
    


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
                    if self.HP + i.regen < self.max_HP:
                        self.HP += i.regen
                    else:
                        self.HP = self.max_HP
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
                p(f"You now have another {item.name}")
            elif x == weapon or x == shield or x == armour:
                p("You already have one")
        else: # If it is not already in bag
            if x == pot: # New pot 
                self.items[item] = 1
                item_added = True
                w(f"{item.name} has been added to your inventory")
            else:
                if x in contents: # if it is not a pot then matching types cannot be bough until an old one is gotten rid off
                    removal = p("Please get rid of your old weapon/shield/armour before purchasing a new one \nWould you like to get rid of an item? (yes/no)",inp=True) # Allow user to delete old item
                    if removal.lower() == "yes":
                        to_be_removed = p("What item would you like removed? (Enter name)",inp=True) # Find item to be deleted
                        for i in all_items:
                            if i.name.lower() == to_be_removed.lower():
                                self.remove_item(i)
                                p("Item was removed") # If it was removed then this message will display
                else:
                    self.items[item] = 1 # If it is not in bag or same type isnt in bag, simply add 1 unit to bag
                    item_added = True
                    if type(item) == weapon:
                        self.AD += item.AD # scale Ad based on items
                    elif type(item) == shield or type(item) == armour:
                        self.HP += item.HP # Scale hp based on items
                        self.max_HP += item.HP
                    w(f"{item.name} has been added to your inventory")
        
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
            opponent = a
            self.battle(opponent)
        elif rand_flt > 0.7 and rand_flt < 0.95: # 25% probability of occurance
            opponent = b
            self.battle(opponent)
        else: #5% probability of occurance
            opponent = c
            self.battle(opponent)

            



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
        if flt < 0.3:
            if val == 26: # Set regions have varying levels of difficulty in terms of enemies
                self.world_map_enemies(enemy(level=1,name=names[1]),enemy(level=2,name =names[2]),enemy(level=3,name =names[3]))
            elif val == 27:
                self.world_map_enemies(enemy(level=4,name =names[4]),enemy(level=5,name =names[5]),enemy(level=6,name =names[6]))
            elif val == 28:
                self.world_map_enemies(enemy(level=7,name =names[7]),enemy(level=8,name =names[8]),enemy(level=9,name =names[9]))
            elif val == 29:
                self.world_map_enemies(enemy(level=10,name =names[10]),enemy(level=11,name =names[11]),enemy(level=12,name =names[12]))
            elif val == 30:
                self.world_map_enemies(enemy(level=13,name =names[13]),enemy(level=14,name =names[14]),enemy(level=15,name =names[15]))
            elif val == 10:
                pass
            else: # If battle is not on world map then use enemies dict. to find right strength enemy
                opponent = enemy(level=val-10,name=names[val-10])
                self.battle(opponent)



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
        elif val == 50: # To enter a door to another map limited by storyline
            self.limiter(placeholder)
        elif val == 40: # To interact with a shop
            self.interact("shop", placeholder)
        elif val == 90: # To interact with a bed
            self.interact("bed", placeholder)
        elif val == 80: # To interact with a story character
            self.interact("storyCharacter",placeholder)
        elif val == 70: # To get across river
            if boat in self.items:
                self.current_location.col -= 1

           



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
            self.limiter(placeholder)
        elif val == 40:
            self.interact("shop", placeholder)
        elif val == 90:
            self.interact("bed", placeholder)
        elif val == 80:
            self.interact("storyCharacter",placeholder)
        elif val == 70: 
            if boat in self.items:
                self.current_location.col += 1
          


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
            self.limiter(placeholder)
        elif val == 40:
            self.interact("shop", placeholder)
        elif val == 90:
            self.interact("bed", placeholder)
        elif val == 80:
            self.interact("storyCharacter",placeholder)
        elif val == 70: 
            if boat in self.items:
                self.current_location.row -= 1
          
          


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
            self.limiter(placeholder)
        elif val == 40:
            self.interact("shop", placeholder)
        elif val == 90:
            self.interact("bed", placeholder)
        elif val == 80:
            self.interact("storyCharacter",placeholder)
        elif val == 70: 
            if boat in self.items:
                self.current_location.row += 1
          