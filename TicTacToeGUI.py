import wx
import glob
from wx.lib.pubsub import pub


#TODO: remove panel as parent for Bitmap class
#or figure out a way to change the grid layout

class TicTacToeGUI(wx.Frame):

	def __init__(self, parent, id, title, controller):
		wx.Frame.__init__(self,parent,id,title)
		
		self.moveMade = None
		self.controller = controller
		'''Game Variables'''
		self.size = 3


		self.parent = parent
		self.panel = wx.Panel(self)

		#grid initialzation
		self.mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
		self.grid = wx.GridSizer(self.size,self.size,10,1)

		#the game pieces
		self.game_pieces = {}
		images = glob.glob('*.jpg')
		for img in images:
			self.game_pieces[img[:-4]] = img

		#the spaces on the board
		self.board = [[None for i in range(self.size)] for i in range(self.size)]
		blank_piece = wx.Image(self.game_pieces['blank'],wx.BITMAP_TYPE_ANY)

		#piece used by user
		self.user_piece = self.game_pieces['player1']

		#initalize the board with empty pieces
		for r in range(self.size):
			for c in range(self.size):
				_temp = TicTacToeBindableBitMapPanel(self.panel,self.game_pieces,self.user_piece, (r,c))
				self.board[r][c] = _temp
				self.grid.Add(_temp, 0, wx.EXPAND)

		self.sendButton = wx.Button(self, wx.ID_CLEAR, "Send")
		self.buttonSizer.Add(self.sendButton, 0, wx.EXPAND)
		self.Bind(wx.EVT_BUTTON, self.send, self.sendButton)

		self.mainSizer.Add(self.grid, 0, wx.EXPAND)
		self.mainSizer.Add(self.buttonSizer, 0, wx.EXPAND)


		self.SetSizerAndFit(self.mainSizer)
		self.buttonSizer.Fit(self.panel)
		self.grid.Fit(self.panel)


		pub.subscribe(self.setMoveMade, "update.moveMade")

		self.initalize()


	def initalize(self):
		self.Show(True)

	def updateBoard(self,data):
		results = data.loads(data)
		board = results['board']
		print(type(board))
		print(board)

	def getMoveMade(self):
		return self.moveMade

	def setMoveMade(self,piece, location):
		self.moveMade = location

	def exportBoard(self):
		board = []
		for r in range(self.size):
			board.append([])
			for c in range(self.size):
				#TODO: fix strings to use self.gamepieces
				print(self.board[r][c].state)
				if(self.board[r][c].state == 'player1'):
					board[r].append(1)
				elif(self.board[r][c].state == 'player2'):
					board[r].append(-1)
				else:
					board[r].append(0)
		return board

	def export(self):
		if(self.moveMade == None):
			return
		board = self.exportBoard()
		data = {'board':board, 'moveMade':self.moveMade}
		self.moveMade = None
		return data

	def send(self, x):
		data = self.export()
		pub.sendMessage('view.update',data=data)

	def updateByModel(self,data):
		boardData = data['board']
		print('Boad Data:',boardData)
		for r in range(self.size):
			for c in range(self.size):
				#TODO: fix strings to use self.gamepieces
				if(boardData[r][c] == 1):
					self.board[r][c].update('player1')
				elif(boardData[r][c] == -1):
					self.board[r][c].update('player2')
				else:
					self.board[r][c].update('blank')

class TicTacToeBindableBitMapPanel(wx.Panel):

	#pieces is a dict of type wx.Image
	#user_piece is wx.Image
	def __init__(self, parent, pieces, user_piece, location):
		wx.Panel.__init__(self,parent)
		self.parent = parent
		self.location = location
		#the current image
		self.state = 'blank'
		self.states = pieces
		
		#the image used by the user
		self.user_piece = user_piece

		self.currentImageMap = wx.StaticBitmap(self,wx.ID_ANY, wx.BitmapFromImage(self.states['blank']))
		self.currentImageMap.Bind(wx.EVT_LEFT_UP, self.onMouseEvent)

	def onMouseEvent(self,event):
		#check if spae is valid
		if(self.state != 'blank'):
			return
		self.state = self.user_piece[:-4]
		self.currentImageMap.SetBitmap(wx.BitmapFromImage(self.user_piece))
		pub.sendMessage("update.moveMade",piece=self.user_piece, location=self.location)
		#self.parent.updateBoard()

	def update(self, new_piece):
		#update the piece with the new piece given (used by parent's update)
		self.state = new_piece
		self.currentImageMap = wx.StaticBitmap(self,wx.ID_ANY, wx.BitmapFromImage(self.states[new_piece]))


if __name__ == "__main__":
    app = wx.App()
    frame = TicTacToeGUI(None,-1,'Tic Tac Toe')
    app.MainLoop()