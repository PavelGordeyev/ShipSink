##################################################################### 
## Author: Pavel Gordeyev
## Date: 8/1/20
## Description:  SinkingShip class definition of the ShipSink game.
#####################################################################
class SinkingShip:

	#####################################################################
	## Description:  Initialize the filled levels and assign the random
	##				 secret word.
	#####################################################################
	def __init__(self, filledLevels,randomWord):
		self.filledLevels = filledLevels
		self.solved = '-' * len(randomWord)

	#####################################################################
	## Description:  Increment the filled levels of the ship by 1
	#####################################################################
	def incFilledLevel(self):
		self.filledLevels += 1

	#####################################################################
	## Description:  Returns the current levels filled in the ship
	#####################################################################
	def getLevelsFilled(self):
		return self.filledLevels

	#####################################################################
	## Description:  Returns the current state of the solved word
	#####################################################################
	def getSolved(self):
		return self.solved

	#####################################################################
	## Description:  Returns a string representation of the ship visual
	#####################################################################
	def getSinkingShip(self):
		# ("______________________________")
		# ("\\___________________________/")
		# (" \\_________________________/")
		# ("  \\_______________________/")
		# ("   \\_____________________/")
		# ("    \\___________________/")
		# ("     \\_________________/")
		# ("      \\_______________/")
		# ("       \\_____________/")
		# ("wwwwwwww\\___________/wwwwwwwwwwww")
		# ("wwwwwwwww\\_________/wwwwwwwwwwwww")
		# ("wwwwwwwwww\\_______/wwwwwwwwwwwwwww")
		# ("wwwwwwwwwww\\_____/wwwwwwwwwwwwwww")
		# ("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")

		# Empty ship array
		shipEmpty = ["_____________________________","\\___________________________/"," \\_________________________/","  \\_______________________/","   \\_____________________/","    \\___________________/","     \\_________________/","      \\_______________/","       \\_____________/","vvvvvvvv\\___________/vvvvvvvvvvvv","vvvvvvvvv\\_________/vvvvvvvvvvvvv","vvvvvvvvvv\\_______/vvvvvvvvvvvvvvv","vvvvvvvvvvv\\_____/vvvvvvvvvvvvvvv","vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"]

		# Filled ship array
		shipFilled = ["_____________________________","\\wwwwwwwwwwwwwwwwwwwwwwwwwww/"," \\wwwwwwwwwwwwwwwwwwwwwwwww/","  \\wwwwwwwwwwwwwwwwwwwwwww/","   \\wwwwwwwwwwwwwwwwwwwww/","    \\wwwwwwwwwwwwwwwwwww/","     \\wwwwwwwwwwwwwwwww/","      \\wwwwwwwwwwwwwww/","       \\wwwwwwwwwwwww/","vvvvvvvv\\wwwwwwwwwww/vvvvvvvvvvvv","vvvvvvvvv\\wwwwwwwww/vvvvvvvvvvvvv","vvvvvvvvvv\\wwwwwww/vvvvvvvvvvvvvvv","vvvvvvvvvvw\\wwwww/vvvvvvvvvvvvvvv","vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"]

		ship = "\n"

		# Concatenate string to create visual of a filled ship up to specified level
		for i in range(0,len(shipEmpty)):
			if i + self.filledLevels < len(shipEmpty) - 1:
				ship += shipEmpty[i] + "\n"
			else:
				ship += shipFilled[i] + "\n"

		return ship

	#####################################################################
	## Description:  Update the state of the solved word
	#####################################################################
	def setWordSolved(self,letter,word):

		arr = list(self.solved)
		arrStr = ""

		for i in range(0,len(word)):
			if letter == word[i]:
				if arr[i] == '-':
					arr[i] = letter

		self.solved = arrStr.join(arr)

	#####################################################################
	## Description:  Return if the game has been won
	#####################################################################
	def isGameOver(self):
		return "-" not in self.solved