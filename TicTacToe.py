T = 'Help'

import pickle

class TicTacToe:

	def __init__(self, size = 3):

		self.board = [[0 for j in range(size)] for i in range(size)]
		self.size = size
		#-1 is player 1's turn
		#1 is player 2's turn
		self.turn = -1


	#encode the game board (change -1 to X and ...)
	def export(self):
		data = pickle.dumps(self.board)
		return data

	#Return false if space is taken, or invalid coord is given
	def setPiece(self, coord):
		x,y = coord
		if(not self.isValid(coord) or self.board[x][y] != 0):
			return False
		self.board[x][y] = self.turn
		self.turn *= -1
		return True

	def isValid(self, coord):
		x,y = coord
		return 0<=x<self.size and 0<=y<self.size

	def updateBoard(self, data):
		pass


if __name__ == "__main__":
	g = TicTacToe()
