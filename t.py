import wx
import sys
import glob

MAIN_PANEL = wx.NewId()


class CommunicationApp(wx.App):
    """This is the class for the communication tool application.
    """

    def __init__(self, config=None, redirect=False):
        """Instantiates an application.
        """
        wx.App.__init__(self, redirect=redirect)
        self.cfg = config
        self.mainframe = CommunicationFrame(config=config,
                                            redirect=redirect)
        self.mainframe.Show()

    def OnInit(self):
        # self.SetTopWindow(self.mainframe)
        return True


class CommunicationFrame(wx.Frame):
    """Frame of the Communication Application.
    """

    def __init__(self, config, redirect=False):
        """Initialize the frame.
        """
        wx.Frame.__init__(self, parent=None,
                          title="CMC Communication Tool",
                          style=wx.DEFAULT_FRAME_STYLE)
        self.imgs = glob.glob('*.jpg')
        self.panel = CommuniationPanel(parent=self,
                                       pid=MAIN_PANEL,
                                       config=config)
        # # Gridbagsizer.
        nrows, ncols = 2, 2
        self.grid = wx.GridSizer(nrows, ncols, 1, 1)
        # Add images to the grid.
        for r in range(0,nrows):
            for c in range(0,ncols):
                _n = ncols * r + c -1
                print('index: ',_n)
                print('len: ',len(self.imgs))
                print(self.imgs[_n])
                _tmp = wx.Image(self.imgs[_n],
                                wx.BITMAP_TYPE_ANY)
                _temp = wx.StaticBitmap(self.panel, wx.ID_ANY,
                                        wx.BitmapFromImage(_tmp))
                self.grid.Add(_temp, 0, wx.EXPAND)

        self.panel.SetSizer(self.grid)
        self.grid.Fit(self)
        
        # set to full screen.
        # self.ShowFullScreen(not self.IsFullScreen(), 0)


class CommuniationPanel(wx.Panel):
    """Panel of the Communication application frame.
    """

    def __init__(self, parent, pid, config):
        """Initialize the panel.
        """
        wx.Panel.__init__(self, parent=parent, id=pid)

        # CALLBACK BINDINGS
        # Bind keyboard events.
        self.Bind(wx.EVT_KEY_UP, self.on_key_up)

    def on_key_up(self, evt):
        """Handles Key UP events.
        """
        code = evt.GetKeyCode()
        print( code, wx.WXK_ESCAPE)
        if code == wx.WXK_ESCAPE:
            sys.exit(0)


def main():
    app = CommunicationApp()
    app.MainLoop()


if __name__ == '__main__':
    main()