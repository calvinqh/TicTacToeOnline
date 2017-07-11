import socketserver
from TicTacToe import *
import random
import pickle

class myRequestHandler(socketserver.BaseRequestHandler):


	def handle(self):
		# self.request is the TCP socket connected to the client
		#retrieve player command
		while(True):
			self.data = self.request.recv(1024).strip()
			coords = self.data.decode("utf-8").split(',')
			coords = [int(i) for i in coords]
			print("Client: ",coords)

			print("{} wrote:".format(self.client_address[0]))
			print(self.data)

			# set piece
			success = game.setPiece(coords)

			#if not good move, prompt user for another coord and end
			if not success:
				message = pickle.dumps('Failed: Try Again')
				self.request.sendall(message)
				return

			#check winner (TODO: make into method)
			winner = game.checkWinner()
			if(winner != 0):
				data = game.exportAll()
				self.request.sendall(data)
				break

			print(game)
			#make computer move (TODO: make into method)
			success = False
			while(not success):
				my_coords = input('>>')
				print(my_coords)
				my_coords = my_coords.split(',')
				my_coords = [int(i) for i in my_coords]
				print("Server: ",my_coords)
				success = game.setPiece(my_coords)

			#check winner (TODO: make into method)
			winner = game.checkWinner()
			if(winner != 0):
				data = game.exportAll()
				self.request.sendall(data)
				break

			#send gameboard
			data = game.exportAll()
			self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    game = TicTacToe()
    server = socketserver.TCPServer((HOST, PORT), myRequestHandler)
    server.serve_forever()