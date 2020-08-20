##################################################################### 
## Author: Pavel Gordeyev
## Date: 8/1/20
## Description:  Simple client-server game called ShipSink.  It is
##				 similar to hangman, except levels of a boat get
##				 filled by pirates, until the ship eventually sinks.
##				 Each wrong guess adds a level of water to the boat.
##
##				 It is a multiplayer game played by (2) clients.
##				 The server acts as the intermediary between (2) 
##				 connecting clients.  It manages the game play and
##				 keeps track of each clients moves and displays each
##				 client's move to the other client.  Only one client
##				 can make a move at a time. 
##
## Sources Used:
## https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
## https://realpython.com/python-sockets/
## https://docs.python.org/3/howto/sockets.html
# https://www.educative.io/edpresso/how-to-convert-strings-to-bytes-in-python
#####################################################################
import random
from ship import *

#####################################################################
## Description:  Setup of the ShipSink game. Initializes the starting
##				 word choices, selects a random word, and creates
##				 an instance of a SinkingShip.  Assembles the 
##				 introductory statement into a single string.
##				 Returns the intro text, reference to the SinkingShip,
##				 and the random secret word.
#####################################################################
def setupShipSink():

	words = ['floaty','paratrooper','mango','banana','physician','cereal']

	# Generate a random word
	randomWord = words[random.randint(0,len(words)-1)]

	# Create instance of a SinkingShip
	ship = SinkingShip(0,randomWord)

	intro = "Here's your ship. It is being attacked by pirates!!!"
	intro += "In order to save it, you must guess the secret word!"
	intro += "If you guess a letter incorrectly, the pirates fill up a level of ship with water!!"
	intro += "If you guess correctly, the pirates will take a short nap till the next guess..."
	intro += "\nBe careful, fill up all 12 levels of the ship and it'll sink!!! :*( "
	intro += "\n\nYou can repeat letters, without penalty only if they are in the word"
	intro += "\n\n ENTER \\q to quit the game at any time...."
	intro += ship.getSinkingShip()

	return (intro,ship,randomWord)

#####################################################################
## Description:  Executes the game play of the ShipSink game.
#####################################################################
def playShipSink(guess,word,ship):

	# Check if the letter guessed is in the word
	if guess in word:
		ship.setWordSolved(guess,word)
		return True
	else: # Increment the filled level of the ship
		ship.incFilledLevel()

	return False