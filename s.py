import socketserver
from TicTacToe import *

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

		#TODO: update gameboard
		success = game.setPiece(coords)

		#TODO: make computer move

		#send gameboard
		data = game.export()
		self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    game = TicTacToe()
    server = socketserver.TCPServer((HOST, PORT), myRequestHandler)
    server.serve_forever()