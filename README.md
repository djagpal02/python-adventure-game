# Python Project - Pixel Adventure

## Introduction

Pixel adventure is a 2D adventure game that takes the user through a story of saving the world, while battling many monsters. The game uses simple turn based battles to allow the user to defeat enemies. The user can do this to gain experience, level up, gain gold and complete missions. Enemies get stronger as the story progresses but the user also has the opportunity to get stronger via leveling up and purchasing items. Each level up comes with a boost in user AD (Attack Damage) and HP (Hit Points). Items serve many functions; some are nessesary for entering particular areas, some give health boosts while in battle and others provide AD or HP boosts. Furthermore, Locations you can visit are locked based on story completion to encourage following the story. Since this game is unlikely to be finished in once sitting, the user has an option to save the game by visiting a bed. This save game can be restored from the start menu and can also be edited manually to change user profile by editing the users txt file. 

## Running the Program

The program was developed in visual studio code using python 3.8.3 but should function just fine on any other IDE. I recommend running from the command line using “python3 main.py” or “python main.py”. Also ensure that the tkinter and pillow libraries are installed. The window size is fixed and requires a minimum screen resolution of 720p. The program was developed in linux but has been tested and is working on windows.


## Getting Started

* To start the game choose wether to load a previous game from save game(txt) or start a new game. 
* Once met with a blank screen press any of "wasd" to get the map to appear. 
* If at any point the game has displayed a message and the user is unable to move, press return/enter to continue. This should allow the user to move again.


## Map Testing

The files contain a "Map Testing Version". This was intended to check the map and ensure all areas are accessible and not causing any issues/errors. This does so by disabling a few of the game features and letting a random number generator decide movement. The differences are:

* Set movement based on random generator
* Remove waiting on print statements
* Remove contin = false after print
* preset inputs to avoid waiting for user input
* remove intro gui and set game = load_game(test) ( fixed to game complete with boat to cross river)
* Remove show_map via gui and use textui instead. - faster due to not needing to load images


## System Testing

I decided on the most important features for the user through playing myself and friends giving opinions. I have a pdf copy of the table containing the results from testing all of these. I made sure to include testing for user input errors as these can be critical if not handled correctly. 


## Unit Testing

I created unit test classes for all my backend classes to ensure correct functionality. A few of these open the gui, as it is integrated in these, and ask for user input. Most inputs can handle random inputs but the fight class will be most effectively handled with an input of 1, thus entering "1" for all inputs is the most effective way to complete these tests.


## Authors and acknowledgment

This game was created by myself, Diljeet Jagpal, for my OO Python Project. Thank you for reading and playing.
