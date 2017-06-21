import wx
import main


class GalleryApp(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 200))

        self.initUI()
        self.Show()

    def initUI(self):
        """Set up the UI."""
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        create_button = wx.Button(panel, 1, "Create Gallery")
        hbox1.Add(create_button, 1, flag=wx.EXPAND|wx.ALL)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.ALL, border=8)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox2.Add(tc, 1, flag=wx.EXPAND | wx.ALL)
        vbox.Add(hbox2, 1, flag=wx.EXPAND | wx.ALL, border=8)

        panel.SetSizer(vbox)


app = wx.App(False)
frame = GalleryApp(None, 'PyGalleryCreator')
app.MainLoop()
