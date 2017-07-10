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


	def __str__(self):
		s = ''
		for i in range(self.size):
			for j in range(self.size):
				s+=str(self.board[i][j])
			s+='\n'
		return s

	#return winner
	#if no winner, return 0
	def checkWinner(self):
		horizontal = True
		h_prev = 0
		vertical = True
		v_prev = 0
		diagonal = True
		winner = 0
		for i in range(1,self.size):
			h_prev = self.board[0][i]
			v_prev = self.board[i][0]
			for j in range(self.size):
				if horizontal and h_prev == self.board[i][j]:
					horizontal = True
				if vertical and v_prev == self.board[j][i]:
					vertical = True
				h_prev = self.board[i][j]
				v_prev = self.board[j][i]
			#check winner
			if vertical or horizontal:
				winner = self.turn *-1 #bc set piece changes turn
				break
		return winner 


if __name__ == "__main__":
	g = TicTacToe()
	g.setPiece((0,0))
	g.setPiece((1,1))
	g.setPiece((1,0))
	g.setPiece((1,2))
	g.setPiece((2,0))
	print(g)
	c = g.checkWinner()
	print(c)