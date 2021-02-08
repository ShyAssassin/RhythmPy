import os

try:
    from Logger import Logger
except ImportError:
    from .Logger import Logger
import platform

# gets home dir + RhythmPy/
def AppDataDir():
    try:
        Platform = platform.system()
        WindowsAppData = str(os.path.expandvars("%appdata%//RhythmPy//"))
        LinuxAppdata = str(os.path.expanduser("~//RhythmPy//"))
        if Platform == "Windows":
            return WindowsAppData
        elif Platform == "Linux" or Platform == "Darwin":
            return str(LinuxAppdata)
        else:
            raise Exception
    except Exception:
        logger = Logger()
        logger = logger.StartLogger(name=__name__)
        logger.exception("failed to get AppDataDir")


# gets home dir + RhythmPy/Config
def AppDataConfigDir():
    try:
        Platform = platform.system()
        WindowsAppDataConfig = str(os.path.expandvars("%appdata%//RhythmPy//Config//"))
        LinuxAppdataConfig = str(os.path.expanduser("~//RhythmPy//Config//"))
        if Platform == "Windows":
            return WindowsAppDataConfig
        elif Platform == "Linux" or Platform == "Darwin":
            return LinuxAppdataConfig
        else:
            raise Exception
    except Exception:
        logger = Logger()
        logger = logger.StartLogger(name=__name__)
        logger.exception("failed to get AppdataConfigDir")
