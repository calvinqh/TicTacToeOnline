import socketserver
from TicTacToeModel import *
import random
import pickle

class myRequestHandler(socketserver.BaseRequestHandler):


	def handle(self):
		# self.request is the TCP socket connected to the client
		#retrieve player command
		while(True):
			self.data = self.request.recv(1024).strip()
			d = pickle.loads(self.data)
			

			# set piece
			success = game.update(self.data)

			#check winner (TODO: make into method)
			winner = game.checkWinner()
			if(winner != 0):
				data = game.exportAll()
				self.request.sendall(data)
				print("Winner: {}".format(game.getWinner()))
				print(game)
				print("User has been disconnected\nGame has been reset.")
				print("")
				game.reset()
				break

			print(game)
			#make computer move (TODO: make into method)
			success = False
			while(not success):
				my_coords = input('>>')
				my_coords = my_coords.split(',')
				my_coords = [int(i) for i in my_coords]
				success = game.setPieceServer(my_coords)

			#check winner (TODO: make into method)
			winner = game.checkWinner()
			if(winner != 0):
				data = game.exportAll()
				self.request.sendall(data)
				print("Winner: {}".format(game.getWinner()))
				print(game)
				print("User has been disconnected\nGame has been reset.")
				print("")
				game.reset()
				break

			#send gameboard
			data = game.exportAll()
			self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    game = TicTacToeModel()
    server = socketserver.TCPServer((HOST, PORT), myRequestHandler)
    server.serve_forever()