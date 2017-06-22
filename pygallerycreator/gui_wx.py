import wx
import main


class GalleryApp(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 200))

        self._init_ui()
        self.Show()

    def _init_ui(self):
        """Set up the UI."""
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        create_button = wx.Button(panel, 1, "Create Gallery")
        create_button.Bind(wx.EVT_BUTTON, self._on_create_click)
        hbox1.Add(create_button, 1, flag=wx.EXPAND | wx.ALL)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.ALL, border=8)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox2.Add(tc, 1, flag=wx.EXPAND | wx.ALL)
        vbox.Add(hbox2, 1, flag=wx.EXPAND | wx.ALL, border=8)

        panel.SetSizer(vbox)

    def _on_create_click(self, e):
        """Get directories and create the gallery."""
        # Get source directory
        source_dir_dialog = wx.DirDialog(self, message="Choose source directory")
        source_dir_dialog.ShowModal()
        source_dir_path = source_dir_dialog.GetPath()

        # Get destination directory
        destination_dir_dialog = wx.DirDialog(self, message="Choose or create destination")
        destination_dir_dialog.ShowModal()
        destination_dir_path = destination_dir_dialog.GetPath()




app = wx.App(False)
frame = GalleryApp(parent=None, title='PyGalleryCreator')
app.MainLoop()
