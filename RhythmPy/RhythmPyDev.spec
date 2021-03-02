# -*- mode: python ; coding: utf-8 -*-
# used for pyinstaller

block_cipher = None


a = Analysis(['__main__.py'],
             pathex=['RhythmPy', "RhythmPy\\Modules"],
             binaries=[],
             datas=[(r'Assets\*.png', 'Assets')],
             hiddenimports=['FixTk', 'tkinter', 'PIL', 'numpy', 'psutil', 'json', 'os', 'sys', 'time', 'cv2', 'threading', 'win32gui', 'win32ui', 'win32con', 'pywin32', 'win32', 'requests', 'inspect', 'functools', 'ctypes', 'logging', 'webbrowser'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='RhythmPyDev',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='RhythmPyDev')
