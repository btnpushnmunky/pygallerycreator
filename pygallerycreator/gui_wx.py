import wx
import main
import os
from wx.lib.delayedresult import startWorker

class GalleryApp(wx.Frame):
    """We simply derive a new class of Frame."""

    def __init__(self, parent, title):
        """Init the frame."""
        wx.Frame.__init__(self, parent, title=title, size=(400, 200))

        os.environ["INTERFACE"] = 'gui'
        self._init_ui()
        self.Show()

    def _init_ui(self):
        """Set up the UI."""
        panel = wx.Panel(self)
        self.timer = wx.Timer(self, 1)
        self.counter = 0
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        create_button = wx.Button(panel, 1, "Create Gallery")
        create_button.Bind(wx.EVT_BUTTON, self._on_create_click)
        self.gauge = wx.Gauge(panel, 1)
        hbox1.Add(create_button, 1, flag=wx.EXPAND | wx.ALL)
        hbox1.Add(self.gauge, 1, flag=wx.EXPAND | wx.ALL)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.ALL, border=8)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox2.Add(self.tc, 1, flag=wx.EXPAND | wx.ALL)
        vbox.Add(hbox2, 1, flag=wx.EXPAND | wx.ALL, border=8)

        panel.SetSizer(vbox)

    def _on_create_click(self, e):
        """Get directories and create the gallery."""
        # Get source directory
        # TODO: Use a progress indicator while processing
        source_dir_dialog = wx.DirDialog(self, message="Choose source directory")
        source_dir_dialog.ShowModal()
        source_dir_path = source_dir_dialog.GetPath()
        self.tc.AppendText("Source: {0}\n".format(source_dir_path))

        # Get destination directory
        destination_dir_dialog = wx.DirDialog(self, message="Choose or create destination")
        destination_dir_dialog.ShowModal()
        destination_dir_path = destination_dir_dialog.GetPath()
        self.tc.AppendText("Destination: {0}\n".format(destination_dir_path))

        self.tc.AppendText("\n")
        self.tc.AppendText("Creating gallery....")
        startWorker(self.work_done, main.create_image_gallery(source_dir_path, destination_dir_path, interface_type="gui"))
        self.timer.Start(100)

    def on_timer(self, e):
        self.counter += 1
        self.gauge.SetValue(self.counter)

    def work_done(self, e):
        self.gauge.SetValue(100)
        self.timer.Stop()
        self.tc.AppendText("Gallery creation finished.")

app = wx.App(False)
frame = GalleryApp(parent=None, title='PyGalleryCreator')
app.MainLoop()
