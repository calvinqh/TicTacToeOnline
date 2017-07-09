import socketserver
from TicTacToe import *

game_board = [' ' for i in range(9)]

class myRequestHandler(socketserver.BaseRequestHandler):


	def handle(self):
		# self.request is the TCP socket connected to the client
		#retrieve player command
		self.data = self.request.recv(1024).strip()

		print("{} wrote:".format(self.client_address[0]))
		print(self.data)

		#TODO: update gameboard

		#TODO: make computer move

		#TODO: send updatedgameboard

		self.request.sendall(bytes(T,'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    game = TicTacToe()
    server = socketserver.TCPServer((HOST, PORT), myRequestHandler)
    server.serve_forever()