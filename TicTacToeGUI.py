import wx
import glob


#TODO: remove panel as parent for Bitmap class
#or figure out a way to change the grid layout

class TicTacToeGUI(wx.Frame):

	def __init__(self, parent, id, title):
		wx.Frame.__init__(self,parent,id,title)
		
 
		'''Game Variables'''
		self.size = 3


		self.parent = parent
		self.panel = wx.Panel(self)

		#grid initialzation
		self.grid = wx.GridSizer(self.size,self.size,10,1)

		#the game pieces
		self.game_pieces = {}
		images = glob.glob('*.jpg')
		for img in images:
			self.game_pieces[img[:-4]] = img

		#the spaces on the board
		self.piece_spaces = []
		blank_piece = wx.Image(self.game_pieces['blank'],wx.BITMAP_TYPE_ANY)

		#piece used by user
		self.user_piece = self.game_pieces['player1']

		#initalize the board with empty pieces
		for r in range(self.size):
			for c in range(self.size):
				_temp = TicTacToeBindableBitMapPanel(self.panel,self.game_pieces,self.user_piece)
				self.piece_spaces.append(_temp)
				self.grid.Add(_temp, 0, wx.EXPAND)
		
		self.panel.SetSizer(self.grid)
		self.grid.Fit(self)

		self.initalize()


	def initalize(self):
		self.Show(True)

	def updateBoard(self,data):
		results = data.loads(data)
		board = results['board']
		print(type(board))
		print(board)


class TicTacToeBindableBitMapPanel(wx.Panel):

	#pieces is a dict of type wx.Image
	#user_piece is wx.Image
	def __init__(self, parent, pieces, user_piece):
		wx.Panel.__init__(self,parent)
		self.parent = root
		#the current image
		self.state = 'blank'
		self.states = pieces
		
		#the image used by the user
		self.user_piece = user_piece

		self.currentImageMap = wx.StaticBitmap(self,wx.ID_ANY, wx.BitmapFromImage(pieces['blank']))
		self.currentImageMap.Bind(wx.EVT_LEFT_UP, self.onMouseEvent)

	def onMouseEvent(self,event):
		#check if spae is valid
		if(self.state == 'used'):
			return
		self.state = 'used'
		self.currentImageMap.SetBitmap(wx.BitmapFromImage(self.user_piece))
		#self.parent.updateBoard()


if __name__ == "__main__":
    app = wx.App()
    frame = TicTacToeGUI(None,-1,'Tic Tac Toe')
    app.MainLoop()