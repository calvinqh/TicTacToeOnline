import socket
import sys
import pickle
from TicTacToe import *


HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])
game = TicTacToe()

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))

while(True):
	
	data = input(">>")
	sock.sendall(bytes(data + "\n", "utf-8"))
	received = sock.recv(1024)
	m = pickle.loads(received)
	#Check if valid move
	if(m == 'Failed: Try Again'):
		print('Try Again')
		continue
	#TODO: check winner?
	
	game.update(received)
	if(game.checkWinner() != 0):
		print("Winner: {}".format(game.getWinner()))
		print("You've been disconnected.")
		break
	print(game)
	#sock.close()

print("To play again reconnect.")
