import platform

Platform = platform.system()
if Platform == "Windows":
    # from .ApplySkins import ApplySkins
    from .WindowCapture import WindowCapture
    from .DirectInput import keyDown, keyUp, press, typewrite
else:
    pass
