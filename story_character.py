import time
all_story_characters = []
from items import basic_sword, hp_pot, earls_gold, boat
from enemy import enemy
from gui import printer as p
from gui import warning as w
from abc import abstractmethod

class story_character:
    def __init__(self, name, key, speech = [], items_gained = [], ):
        self.name = name
        self.key = key 
    
        all_story_characters.append(self)
        
#######################################################  TOWN 1 and CAVE #########################################################################33


############################################################## Mom ###########################################################################
class mom(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    @abstractmethod
    def interact(self,player):
        if player.story_tracker == 1: # Until spoken to leader
            p(f"Good Morning {player.name}! \nChief wants to speak to you, maybe you should go over to his house \nMake sure your safe, its getting really bad out there...")
        elif player.story_tracker == 2 or player.story_tracker == 3:
            p(f"Be careful out there son...")
        elif player.story_tracker > 3:
            p("Thank you son, you have really made us proud!!")


Mom = mom("Mom", "PARNT")

############################################################# Chief ##############################################################################
class chief(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker == 1: 
            p("""I see you got my message...
            I wish we were meeting under better circumstances but here it is...
            The village is being terrorised by Wolfernius, he is eating our livestock
            You are our last chance...
            I hear he comes from a cave not far, south-west of here.
            Speak to John before heading out. I have given him a few things for you...
            Good luck and safe journey!""")
            player.story_tracker = 2
        elif player.story_tracker == 2 or player.story_tracker == 3:
            p(f"Good Luck {player.name}, we are all counting on you...")
        elif player.story_tracker > 3:
            p("""YOU HERO!!!
            You have saved our village!
            I dont know much about this Drakthor, but maybe Chief Earl from 2TOWN does...""")


Chief = chief("Chief", "CHIEF")
########################################################### John ###############################################################################
class john(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker == 1:
            p("Apprently the Chief was looking for you, I think he is at home...")
        elif player.story_tracker == 2:
            p("""If your heading out of town, prepare youself.
            There are monsters everywhere and they will not think twice before attacking you...
            Heres a sword and a health potion to help you on your journey""")
            player.add_item(hp_pot)
            player.add_item(basic_sword)
            player.story_tracker = 3
        elif player.story_tracker == 3:
            p("Good luck...")
        elif player.story_tracker > 3:
            p("YOUR A HEROOO!!!!!")


John = john("John", "JOHN-")

######################################################### wolfernius ########################################################################
class wolfernius(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <= 3:
            p("""You better have brought me some sheep...
            I guess you will have to do""")
            opponent = enemy(5, "Wolfernius")
            winner = player.battle(opponent)
            time.sleep(2)
            if winner == player.name:
                player.story_tracker = 4
                p("""You win, I will stop taking your sheep... 
                But if you think it ends here... HAH...
                Dark times are coming...
                When Drakthor takes final form...
                I will be back ... *cough*""")
            else:
                p("""HA!...
                YOU THOUGHT YOU COULD DEFEAT ME...""")
        elif player.story_tracker > 3:
            p("""You win, I will stop taking your sheep... 
            But if you think it ends here... HAH...
            Dark times are coming...
            When Drakthor takes final form...
            I will be back ... *cough*""")


Wolfernius = wolfernius("Wolfernius", "WOLFS")

########################################################### TOWN 2 AND TOWER ####################################################################


########################################################## EARL ############################################################################
class earl(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker == 4:
            p("""You want to know about Drakthor...
            I might know something that could help...
            But you'll have to do something for me...
            Someone has stolen my gold and I need you to get it back...
            It will be worth your time, I promise.
            Ask around town, maybe someone knows something that might help.""")
            player.story_tracker = 5
        elif player.story_tracker == 5:
            p("Come on now, find me that gold !")
        elif player.story_tracker == 6:
            p(f"""Incredible...
            I wasnt sure you would make it but here you are!
            As promised here is some gold for your hard work...
            {player.name} got 2000 gold
            About Drakthor...
            I don't personally know a great deal but ...
            I have heard Drakthor is from Town3, maybe you should check it out...""")
            player.gold += 2000
            player.remove_item(earls_gold)
            player.story_tracker = 7
        else:
            p("""About Drakthor...
            I don't personally know a great deal but ...
            I have heard Drakthor is from Town3, maybe you should check it out...""")
            
    
Earl = earl("Earl", "EARL-")

########################################################## Tom ##############################################################################

class tom(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker == 5:
            p("""Apprently the Serpant Queen took Earls gold...
            But what do I know?""")
        else:
            p("""WOW!
            You truly are a warrior!!!""")

Tom = tom("Tom", "2TOM2")

######################################################  Rebecca #############################################################################

class rebecca(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker == 5:
            p("""I heard the gold stashed at a tower just North-East of here....
            Maybe you should take a look...
            Careful, the tower is no place for games, dark forces are present there...""")
        else:
            p("""I can not belive it...
            Good Job!""")

Rebecca = rebecca("Rebecca", "RBKKA")

##################################################### Serpant Queen #########################################################################

class serpant_queen(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <= 5:
            p("""SSSSSSSSsssssssssssssssssssssso you thinksss you can take my goldssss...
            thinkssss AGAIN!""")
            opponent = enemy(10, "Serpant Queen")
            winner = player.battle(opponent)
            time.sleep(2)
            if winner == player.name:
                player.story_tracker = 6
                p("""SSSssuch power...
                Get AWAY FROM ME!
                Drakthor will give me power...
                You will SSSSssseeeee....""")
                player.add_item(earls_gold)
            else:
                p("""So...
                PATHETIC""")
        elif player.story_tracker > 5:
            p("""You got your gold...
            What do you want from me...""")

Serpant_queen = serpant_queen("Serpant Queen", "SRPQN")



#########################################################  TOWN 3  ###############################################################################3

#########################################################  Minion  ############################################################################

class minion(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker == 7:
            p("By Lord Drakthor you shall not pass")
            opponent = enemy(15, "Drakthor's Minion")
            winner = player.battle(opponent)
            time.sleep(2)
            if winner == player.name:
                player.story_tracker = 8
                p("In the end, Drakthor will still remain victorious...")
            else:
                p("YOU DO NOT STAND A CHANGE AGAINST THE MIGHTY DRAKTHOR")
        elif player.story_tracker > 7:
            p("In the end, Drakthor will still remain victorious... **Cough**")
        
Minion = minion("Minion", "MNIMN")

#########################################################  Mayor Quinby  ######################################################################

class mayor(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <= 7:
            p("I... Ca..n't... speak....Drakt..hor...")
        elif player.story_tracker > 7:
            p("""Thank you for saving our town.
            I can tell you more about Drakthor...
            He used to be one of our own, but he took a dark turn...
            Using an Ancient ritual, he will be turning himself into a dragon...
            The new form comes with many powers and control over the darkworld...
            If he succeeds then it is the end for us all...
            I dont know when, but I know it will be ontop mount Bloodspike
            But to get there you will need to cross the red river...""")

Mayor = mayor("Mayor Quinby", "MAYOR")

#########################################################  Ben  ############################################################################

class ben(story_character):
    def __init__(self, name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <= 7:
            p("HELPPP!!!")
        elif player.story_tracker > 7:
            p("If you need to get across the river, maybe you could get a boat from Queen Rachel of Town 4")

Ben = ben("Ben", "BENNN")

####################################################  TOWN 4  ##########################################################################################

####################################################  QUEEN  ###################################################################################
class queen(story_character):
    def __init__(self,name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <=8:
            p("""I can give you a boat...
            but you have to do something for me in return.
            I need you to defeat Sion, the beast at CAVE 4
            All my men are too scared to go anywhere near that cave, if you do this the boat is yours.""")
        elif player.story_tracker == 9:
            p("""Unbelieveable...
            As I promised here is your boat """)
            player.add_item(boat)
            player.story_tracker = 10
        else:
            p("Your mission is perilous, good luck to you...")
        
Queen = queen("Queen Rachel", "QUEEN")

##################################################### Royal Guard ###################################################################################
class guard(story_character):
    def __init__(self,name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <=8:
            p("""If your looking for the Queen, she is inside...
            If your looking for CAVE 4, it is south-east of here""")
        else:
            p("Everyone is so relieved since you defeated Sion, thank you!!")

Guard = guard("Royal Guard", "GUARD")

#####################################################  SION  #####################################################################################
class sion(story_character):
    def __init__(self,name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <= 8:
            p("""You DARE come to my lair...
            BIG MISTAKE!""")
            opponent = enemy(20, "Sion")
            winner = player.battle(opponent)
            time.sleep(2)
            if winner == player.name:
                player.story_tracker = 9
                p("""WHO ARE YOU???
                I will leave Queen Rachel alone...
                Just please dont hurt me anymore...""")
            else:
                p("""DRAKTHOR WILL DRINK THE BLOOD OF HIS ENEMIES
                I SHALL FEAST BY HIS SIDE""")
        elif player.story_tracker > 8:
            p("I wil do whatever you want...")

Sion = sion("Sion", "SIONN")
###########################################################  MNTN  ###########################################################################################

########################################################### Mountain village folk #############################################################

class frosty(story_character):
    def __init__(self,name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <=10:
            p("""The end is near...
            Tonight Drakthor becomes DRAGONTHOR!
            Best thing to do...
            RUN!!!
            If you want to find him, hes at the very top""")
        else:
           p("Bringiner of light, I THANK YOU !!")


Frosty = frosty("Frosty Fred", "FROST")

###########################################################  DRAKTHOR #######################################################################

class drakthor(story_character):
    def __init__(self,name, key):
        super().__init__(name, key)

    def interact(self,player):
        if player.story_tracker <=10:
            p("""THE END IS HERE!
            YOU CANNOT STOP THIS!
            MY MINION WILL SLAY YOU""")
            opponent = enemy(25, "Drakthor's Minon")
            winner = player.battle(opponent)
            time.sleep(2)
            if winner == player.name:
                p("""Well done against my minion, maybe I underestimated you...")
                HE IS HERE!!
                DRAGONTHOR!
                DRAGONTHOR:
                LETS TEST MY NEW STRENGTH ON YOU""")
                opponent = enemy(35, "DRAGONTHOR")
                winner = player.battle(opponent)
                time.sleep(2)
                if winner == player.name:
                    p("""Thank you for playing.
                    Hope you enjoyed this game
                    By Diljeet Jagpal""")
                    player.story_tracker = 11
                else:
                    p("YOU DO NOT STAND A CHANGE AGAINST THE MIGHTY DRAKTHOR")
            else:
                p("YOU DO NOT STAND A CHANGE AGAINST THE MIGHTY DRAKTHOR")
            

DRK = drakthor("Drakthor", "DRKTH")

