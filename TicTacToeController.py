from TicTacToeModel import *
from TicTacToeGUI import *
from wx.lib.pubsub import pub
import socket
import pickle

class TicTacToeController:

	def __init__(self):
		self.app = wx.App()
		self.view = TicTacToeGUI(None,-1,'Tic Tac Toe',self)
		pub.subscribe(self.send, 'view.update')
		pub.subscribe(self.updateView, 'model.update')
		self.model = TicTacToeModel()
		self.sock = None

	def send(self,data):
		self.model.updateByGUI(data)
		print('GUI',data)
		data = self.model.exportAll()
		print(self.sock)
		self.sock.sendall(data)
		recieved = self.sock.recv(1024)
		m = pickle.loads(recieved)
		print(m)
		self.model.update(recieved)
		#self.model.update(recieved)

	def updateView(self,data):
		print("Recived message")
		self.view.updateByModel(data)

	def start(self,socket):
		print(socket)
		if(self.sock == None):
			self.sock = socket
		self.app.MainLoop()



if __name__ == "__main__":
	'''
	g = TicTacToe()
	g.setPiece((0,1))
	g.setPiece((0,0))
	g.setPiece((1,1))
	g.setPiece((1,0))
	g.setPiece((2,1))

	c = g.checkWinner()
	print(g)
	print(g.checkWinner())

	app = wx.App()
	frame = TicTacToeGUI(None,-1,'Tic Tac Toe')
	app.MainLoop()
	'''

	g = TicTacToeController()