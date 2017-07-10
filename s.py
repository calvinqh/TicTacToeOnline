import socketserver
from TicTacToe import *
import random
import pickle

class myRequestHandler(socketserver.BaseRequestHandler):


	def handle(self):
		# self.request is the TCP socket connected to the client
		#retrieve player command
		self.data = self.request.recv(1024).strip()
		coords = self.data.decode("utf-8").split(',')
		coords = [int(i) for i in coords]
		print(coords)

		print("{} wrote:".format(self.client_address[0]))
		print(self.data)

		# set piece
		success = game.setPiece(coords)
		#if not good move, prompt user for another coord and end
		if not success:
			message = pickle.dumps('Failed: Try Again')
			self.request.sendall(message)
			return

		#make computer move
		success = False
		while(not success):
			x = random.randint(0,2)
			y = random.randint(0,2)
			coords = [x,y]
			success = game.setPiece(coords)

		#send gameboard
		data = game.export()
		self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    game = TicTacToe()
    server = socketserver.TCPServer((HOST, PORT), myRequestHandler)
    server.serve_forever()