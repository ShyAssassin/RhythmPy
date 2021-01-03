# -*- mode: python ; coding: utf-8 -*-	
# used for pyinstaller	

block_cipher = None	


a = Analysis(['__main__.py'],	
             pathex=['C:\\Users\\Assassin\\Documents\\GitHub\\RhythmPy\\RhythmPy', "C:\\Users\\Assassin\\Documents\\GitHub\\RhythmPy\\RhythmPy\\Modules"],	
             binaries=[],	
             datas=[(r'C:\Users\Assassin\Documents\GitHub\RhythmPy\RhythmPy\UI-Media\*.png', 'UI-Media')],	
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
          name='RhythmPy',	
          debug=False,	
          bootloader_ignore_signals=False,	
          strip=False,	
          upx=True,	
          console=False )	
coll = COLLECT(exe,	
               a.binaries,	
               a.zipfiles,	
               a.datas,	
               strip=False,	
               upx=True,	
               upx_exclude=[],	
               name='RhythmPy')