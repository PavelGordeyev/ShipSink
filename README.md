# ShipSink
Simple client-server game. 

It is similar to hangman, except levels of a boat get filled by pirates, until the ship eventually sinks. 
Each wrong guess adds a level of water to the boat. 

### Gameplay
It is a multiplayer game played by (2) clients. 

The server acts as the intermediary between (2) connecting clients.  

It manages the game play and keeps track of each clients moves and displays each client's move to the other client.  

Only one client can make a move at a time. 

### Instructions for running the game
1. Open (3) terminal windows
2. In each, navigate to the directory where the files for the extra credit project were saved 3. First, enter “python3 shipSink-server.py” in one of the terminal windows
a. This starts up the server to host the game
4. Next, enter “python3 shipSink-client.py” in one of the other windows – CLIENT 1
a. This connects the first client to the server to play the game
b. The server is waiting for (2) players to join
5. Next, enter “python3 shipSink-client.py” in the final window that hasn’t been used yet
– CLIENT 2
a. This will trigger the start of the game and you should see a welcome message
and some prompts
6. CLIENT-1 will be the first to go and is thus prompted in its window for a guess
7. Meanwhile, CLIENT-2 has a message telling it that it is waiting for the other player/client
to make a move
8. Continue entering guesses between the CLIENT-1 and CLIENT-2 windows until you
either win or lose
a. The connections will close once the game is over
9. If you want to quit, you may enter in “/q” at any time in either CLIENT-1 or CLIENT-2
