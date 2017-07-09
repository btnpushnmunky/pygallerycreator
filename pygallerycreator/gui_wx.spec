# -*- mode: python -*-

block_cipher = None


a = Analysis(['gui_wx.py'],
             pathex=['C:\\Users\\Dan\\Projects\\PyGalleryCreator\\pygallerycreator'],
             binaries=[],
             datas=[('vendor', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PyGalleryCreator',
          debug=False,
          strip=False,
          upx=False,
          console=False)
