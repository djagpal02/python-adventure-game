from random import random
from gui import printer as p



class fight:
    """
    A class to represent a fight between user and randomized bot

    Even though this has no arguments, this class is usefull to create new fight "events" without having to set everything up each time. 
    ...

    Methods
    -------
    battle(player, opponent)
        The function that carries out the battle, taking in user input along with randomized opponent attacks.
    full_battle(player, opponent)
        Takes the results of the battle and applies all post battle requirements, ie looting gold and items, adding exp, if dead taking to last save game
    """



    def battle(self, player, opponent):
        """
        The function that carries out the battle, taking in user input along with randomized opponent attacks.
        ...

        Parameters
        ----------
        :param player: game user
        :type player: player.character
        :param opponent: the computer generated bot
        :type opponent: enemy

        Return
        ------
        :return winner: returns the name of the winner
        :return type: str
        """
        winner = None  # Set winner equal to None, incase player decides to run away
        while winner == None:   # When a new winner is set the battle is over 
            opponent.attack(player) # Since enemies suprise the player, they get to attack first
            if player.HP <= 0: # Check if somone has won 
                winner = opponent.name
                p(f"{player.name} has been defeated.")
                break
            next_move = input("What is your next move? 1 = attack, 2 = use item , 3 = try to run ")
            if next_move == "1": # If user chooses to retaliate
                player.attack(opponent)
                if opponent.HP <= 0: # Check if somone has won
                    winner = player.name
                    p(f"{opponent.name} has been defeated.")
            elif next_move == "2": # If user chooses to use an item
                item_selected = False # To ensure an item is actually selected and to loop around if it is not
                while item_selected == False:
                    p("You have:") # Print items available
                    for i in player.items:
                        p(i.name)   
                    # Item selection or exit
                    x = input("Which item would you like to use? type exit to return to battle ")
                    if x == "exit":
                        item_selected = True
                    else: 
                        outcome = player.use_item(x)
                        if outcome == True:
                            item_selected = True
                            p(f"{x} was used")
                        else:
                            p("Invalid Input")
            elif next_move == "3": # If user chooses to try and run away
                value = random() # Generate float between 0 and 1
                if value > 0.75: # To make it a 25% chance of success
                    p("You got away")
                    winner = "No winner"
                else:
                    p("You got blocked")
            else: # If entry was invalid
                p("Invalid entry, while you were choosing your were attacked....")

        return winner
    


    def full_battle(self, player, opponent):
        """
        Takes the results of the battle and applies all post battle requirements, ie looting gold and items, adding exp, if dead taking to last save game
        ...

        Parameters
        ----------
        :param player: game user
        :type player: player.character
        :param opponent: the computer generated bot
        :type opponent: enemy
        """
        winner = self.battle(player, opponent) # Assign outcome of battle to winner
        if player.name == winner: # If user has won
            for i in opponent.items:
                player.add_item(i)
            player.gold += opponent.gold # Steal enemies gold
            player.exp_gain(opponent) # Gain experinece points 
            p(f"{player.name} wins..... {player.name} loot {opponent.gold} and {opponent.items}")
        elif opponent.name == winner: # If user has been killed
            p("You will be taken to your last save location")
            player.death()
