##################################################################### 
## Author: Pavel Gordeyev
## Date: 8/1/20
## Description:  Server portion of the ShipSink game.  Sets up and
##				 runs the game between exactly (2) clients.  It
##				 handles processing the client inputs and shows the
##				 results of each turn to each client.
##
## Sources Used:
## https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
## https://realpython.com/python-sockets/
## https://docs.python.org/3/howto/sockets.html
# https://www.educative.io/edpresso/how-to-convert-strings-to-bytes-in-python
#####################################################################
import socket
from shipGame import *

def main():

	# Server information
	HOST = '127.0.0.1'
	PORT = 7199
	MAX_REQ = 2
	conn = 0

	# Create the server-side socket
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket
	serverSocket.bind((HOST,PORT))

	# Queue up to MAX_REQ connections
	serverSocket.listen(MAX_REQ)

	print("Server listening on: localhost on port: ", PORT)

	(welcomeMessage,ship,word) = setupShipSink()

	# Establish 2 connections; one for each player and then begin the game
	while(conn < 2):
		if conn == 0:
			# Accept connection
			(clientSocket, address) = serverSocket.accept()
		else:
			# Accept connection
			(clientSocket2, address) = serverSocket.accept()

		conn += 1

		print("Connected by ", address)

	
	try:
		# Get the message from the client
		res = clientSocket.recv(2048)
		res2 = clientSocket2.recv(2048)

		# Send welcome message
		clientSocket.sendall(bytes(welcomeMessage,'utf-8'))
		clientSocket2.sendall(bytes(welcomeMessage,'utf-8'))

		# Receive the "ok"
		res = clientSocket.recv(2048)
		res2 = clientSocket2.recv(2048)
	except BrokenPipeError:
		serverSocket.close()
	else:
		turn = 0
		mess = ""

		while(1):

			if turn % 2 == 0:
				# Notify clients to either "wait" their turn or "go" ahead with their move
				clientSocket.sendall(bytes("go",'utf-8'))
				clientSocket2.sendall(bytes("wait",'utf-8'))

				# Get the message from the clients
				res = clientSocket.recv(2048)
				clientSocket2.recv(2048)

				# Checks if client exited and closed the connection
				if res.decode("utf-8") == "/q":
					clientSocket2.sendall(bytes("Other player exited...Game is over now!",'utf-8'))
					res = clientSocket2.recv(2048)
					break

			else:
				# Notify clients to either "wait" their turn or "go" ahead with their move
				clientSocket.sendall(bytes("wait",'utf-8'))
				clientSocket2.sendall(bytes("go",'utf-8'))

				# Get the message from the client
				res = clientSocket2.recv(2048)
				clientSocket.recv(2048)

				# Checks if client exited and closed the connection
				if res.decode("utf-8") == "/q":
					clientSocket.sendall(bytes("Other player exited...Game is over now!",'utf-8'))
					res = clientSocket.recv(2048)
					break

			if playShipSink(res.decode("utf-8"),word,ship):
				mess = "\nAHOY! WELL DONE!!!!\nGuess was: " + res.decode("utf-8") + "\n\nSecret Word: " + ship.getSolved()

				if ship.isGameOver():
					mess = "\n*********!!!!********\nYou won and your ship didn't sink!!\nThe secret word was: " + word + "\n\n"
					clientSocket.sendall(bytes(mess,'utf-8'))
					clientSocket2.sendall(bytes(mess,'utf-8'))
					break
			else:
				if ship.getLevelsFilled() < 12:
					mess = "\nAY! THAT'S NOT IN THE WORD!!!\n" + ship.getSinkingShip() + "\n\nGuess was: " + res.decode("utf-8") + "\n\nSecret Word: " + ship.getSolved()
				else:
					mess = ship.getSinkingShip() + "\n\nGuess was: " + res.decode("utf-8") + "\n\nOh no! The pirates filled up the ship full of water and it sank! Womp womp! Better luck next time...\n\nThe secret word was: " + word + "\n"
					clientSocket.sendall(bytes(mess,'utf-8'))
					clientSocket2.sendall(bytes(mess,'utf-8'))
					break


			# Send response message to both clients
			clientSocket.sendall(bytes(mess,'utf-8'))
			clientSocket2.sendall(bytes(mess,'utf-8'))

			# Receive message back from client to be able to send out next prompt
			clientSocket.recv(2048)
			clientSocket2.recv(2048)

			turn += 1

		serverSocket.close()
	
# Call main function
if __name__ == "__main__":
	main()