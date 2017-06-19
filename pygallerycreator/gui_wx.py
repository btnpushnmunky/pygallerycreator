import wx
import main


class GalleryApp(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 200))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.button = wx.Button(self, -1, "Create Gallery")
        hbox.Add(self.button, border=50)
        self.SetSizer(hbox)
        self.Show(True)

app = wx.App(False)
frame = GalleryApp(None, 'PyGalleryCreator')
app.MainLoop()
