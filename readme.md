**Github Status**
[![Build Status](https://travis-ci.org/btnpushnmunky/pygallerycreator.svg?branch=master)](https://travis-ci.org/btnpushnmunky/pygallerycreator.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/btnpushnmunky/pygallerycreator/badge.svg?branch=master)](https://coveralls.io/github/btnpushnmunky/pygallerycreator?branch=master)

**Gitlab Status**
[![build status](https://gitlab.com/dsross/PyGalleryCreator/badges/master/build.svg)](https://gitlab.com/dsross/PyGalleryCreator/commits/master) [![coverage report](https://gitlab.com/dsross/PyGalleryCreator/badges/master/coverage.svg)](https://gitlab.com/dsross/PyGalleryCreator/commits/master)

*Note: Only master is building.*

A utility to create web galleries from a directory of images
============================================================

**Requirements**

Python 3

Requirements in requirements.txt

Automatic Image Montage (included in repo)
https://tympanus.net/codrops/2011/08/30/automatic-image-montage/

Lightbox (included in repo)
http://lokeshdhakar.com/projects/lightbox2/#options

**Full gallery view**

![Alt text](screenshot1.png?raw=true)

**Image in Lightbox**

![Alt text](screenshot2.png?raw=true)


GUI
======
The GUI uses wxPython. It *should* build with PyInstaller as long as you run `pyinstaller gui_wx.spec -w --noupx` from the pygallerycreator directory.
Get your .exe from the dist folder.

Prior to building, you'll need to adjust the gui_wx.spec folder to match your user paths.