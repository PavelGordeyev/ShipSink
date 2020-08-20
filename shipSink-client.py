##################################################################### 
## Author: Pavel Gordeyev
## Date: 8/1/20
## Description:  Client portion of the ShipShink game.  It allows a
##				 client to connect to a previously specified port
##				 on the localhost to play the game against another
##				 client.
##
## Sources Used:
## https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
## https://realpython.com/python-sockets/
## https://docs.python.org/3/howto/sockets.html
# https://www.educative.io/edpresso/how-to-convert-strings-to-bytes-in-python
#####################################################################
import socket

def main():

	# Server information
	HOST = '127.0.0.1'
	PORT = 7199

	# OK Message
	messageOK= "ok"

	# Create the client-side socket
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to the server
	clientSocket.connect((HOST,PORT))

	print("Connected to: ", "localhost", "on port: ", PORT)
	print("Waiting for all players to join...")

	# Send to server upon connecting
	clientSocket.sendall(bytes("play",'utf-8'))

	# Get the welcome message
	res = clientSocket.recv(2048)
	print(res.decode("utf-8"))

	# Send the "ok" after welcome message
	clientSocket.sendall(bytes(messageOK,'utf-8'))

	while(1):
		
		# Receive response
		try:
			res = clientSocket.recv(2048)
		except (BrokenPipeError,ConnectionResetError):
			break

		# Validate the response
		if res != b'':

			# Check if the server instructed to wait or to make a move
			if res.decode("utf-8") == "wait":
				print("Waiting for the other player to make a move...")
				message = messageOK
			elif res.decode("utf-8") == "go":
				message = input("Enter a letter: ")
			else: # Generic reponse for not a "wait" or a "go"
				print(res.decode("utf-8"))
				message = messageOK

		# Send response message; aka the player's guess or an "ok" message
		try:
			clientSocket.sendall(bytes(message,'utf-8'))
		except (BrokenPipeError,ConnectionResetError,OSError):
			break

		if message == "/q":
			print("Pirates have other duties to attend to anyway....Till next time!")
			break

	clientSocket.close()		

# Call main function
if __name__ == "__main__":
	main()