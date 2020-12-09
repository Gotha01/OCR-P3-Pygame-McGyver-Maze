# Projet3
Mac Gyver Game
MAZE:**
(It is a on level maze) Help MacGyver to escape the maze!

Size: It’s a 15x15 maze.

1 sprite = 30x30 pixels

Uses: Use the arrows from your keyboard to move the player inside the structure.

Goal: You need to collect all of the 3 items (a needle, a pipe and ether) to build a syringe and put the guard to sleep. That’s his only way to go out! You just need to go on the top of an item to collect it. It will directly go to your inventory.

If you meet the guard without all 3 items, the guard will kill you. At the moment that your player is front of the guard, the game stops and a window says you if you have win or lose. You need to close the window and restart the game to play one more time. The items change their places at each new start of the game.

RUN THE GAME:

Installation required:

Install Virtual Environment : python -m pip venv env
Inside the folder "setting" open the file "install.py" !! Don’t forget to run cmd or powershell as administrator !
Launch:

To start the game after that, launch main.py
FEATURES:

Encoding: Python 3

Launched: Pygame (works with Pygame 1 and 2)

Fork: https://github.com/Gotha01/Projet3.git



DESCRIPTION:

Folder

resources	      Contain all the necessary images to build the project

Python files

install.py	    File to install “requirement.txt”
mcgyver.py	    Class MacGyver
constants.py    Constant necessaries in the game
accessor.py	    Import of all the classes to structure the global game
maze.py	        Class Laze to analyse "level_table.py" and create all the method necessary to run the maze structure
visual.py	      Loading of the images and initiate the texts necessaries in the game
main.py	        File to start the game
level_table.py	Structure of the maze (“M” for McGyver, “G” for Guardian, “O” for walls and “.” for path)

Text files
requirement.txt	


TO CONTRIBUTE:

You need to respect PEP8 !!!

Fork it

Create your feature branch

Commit your changes

Push to your branch

Create a pull request

WRITTEN BY:
Gotha01
