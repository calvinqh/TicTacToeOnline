import socketserver
from TicTacToe import *

class myRequestHandler(socketserver.BaseRequestHandler):


	def handle(self):
		# self.request is the TCP socket connected to the client
		#retrieve player command
		self.data = self.request.recv(1024).strip()

		print("{} wrote:".format(self.client_address[0]))
		print(self.data)

		#TODO: update gameboard

		#TODO: make computer move

		#send gameboard
		data = game.export()
		self.request.sendall(data)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    game = TicTacToe()
    server = socketserver.TCPServer((HOST, PORT), myRequestHandler)
    server.serve_forever()