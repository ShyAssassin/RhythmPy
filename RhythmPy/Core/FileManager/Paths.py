import os
import platform

# gets home dir + RhythmPy/
def AppDataDir():
    """
    Gets the folder where files are to be stored based on running OS
    """
    try:
        Platform = platform.system()
        WindowsAppData = str(os.path.expandvars("%appdata%//RhythmPy//"))
        LinuxAppdata = str(os.path.expanduser("~//RhythmPy//"))
        if Platform == "Windows":
            return str(WindowsAppData)
        elif Platform == "Linux" or Platform == "Darwin":
            return str(LinuxAppdata)
        else:
            raise Exception
    except Exception:
        print("failed to get AppDataDir")


# gets home dir + RhythmPy/Config
def AppDataConfigDir():
    """
    Gets the folder where Config files are to be stored based on running OS
    """
    try:
        Platform = platform.system()
        WindowsAppDataConfig = str(os.path.expandvars("%appdata%//RhythmPy//Config//"))
        LinuxAppdataConfig = str(os.path.expanduser("~//RhythmPy//Config//"))
        if Platform == "Windows":
            return str(WindowsAppDataConfig)
        elif Platform == "Linux" or Platform == "Darwin":
            return str(LinuxAppdataConfig)
        else:
            raise Exception
    except Exception:
        print("failed to get AppdataConfigDir")


# gets home dir + RhythmPy/Logs
def AppDataLogsDir():
    """
    Gets the folder where Log files are to be stored based on running OS
    """
    try:
        Platform = platform.system()
        WindowsAppDataLogs = str(os.path.expandvars("%appdata%//RhythmPy//Logs//"))
        LinuxAppdataLogs = str(os.path.expanduser("~//RhythmPy//Logs//"))
        if Platform == "Windows":
            return str(WindowsAppDataLogs)
        elif Platform == "Linux" or Platform == "Darwin":
            return str(LinuxAppdataLogs)
        else:
            raise Exception
    except Exception:
        print("failed to get AppDataLogsDir")
