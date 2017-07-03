
A utility to create web galleries from a directory of images
============================================================



**Requirements**

I've been using Anaconda's Python 3 distribution: https://www.continuum.io/downloads

Create a Python 3 environment once you've installed Python.

Then:

* `pip install -r requirements.txt` 
* `pip install git+https://github.com/pyinstaller/pyinstaller.git`

If you're building on Windows, you may need to install `pywin32`. To do so: `conda install pywin32==220`.

To build the gui:

* Adjust `gui_wx.spec` to match your file paths.
* Run `pyinstaller gui_wx.spec` from inside the pygallercreator directory.

Get your .exe from the dist folder.

**Full gallery view**


![Alt text](screenshot1.png?raw=true)


**Image in Lightbox**



![Alt text](screenshot2.png?raw=true)


**Vendor Files Included**

Automatic Image Montage: https://tympanus.net/codrops/2011/08/30/automatic-image-montage/

Lightbox: http://lokeshdhakar.com/projects/lightbox2/#options