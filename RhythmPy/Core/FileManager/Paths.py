import os
import platform

# gets home dir + RhythmPy/
def AppDataDir():
    """Gets the folder where files are to be stored based on running OS"""
    try:
        Platform = platform.system()
        if Platform == "Windows":
            WindowsAppData = str(os.path.expandvars("%appdata%//RhythmPy//"))
            return str(WindowsAppData)
        elif Platform == "Linux" or Platform == "Darwin":
            LinuxAppdata = str(os.path.expanduser("~/.RhythmPy/"))
            return str(LinuxAppdata)
        else:
            raise Exception
    except Exception:
        print("failed to get AppDataDir")


def PluginsDir():
    """Gets the folder where plugins are to be stored based on running OS"""
    try:
        Platform = platform.system()
        if Platform == "Windows":
            WindowsPlugins = str(os.path.expandvars("%appdata%//RhythmPy//Plugins//"))
            return str(WindowsPlugins)
        elif Platform == "Linux" or Platform == "Darwin":
            LinuxPlugins = str(os.path.expanduser("~/.RhythmPy/Plugins/"))
            return str(LinuxPlugins)
        else:
            raise Exception
    except Exception:
        print("failed to get PluginsDir")


# gets home dir + RhythmPy/Config
def AppDataConfigDir():
    """Gets the folder where Config files are to be stored based on running OS"""
    try:
        Platform = platform.system()
        if Platform == "Windows":
            WindowsAppDataConfig = str(
                os.path.expandvars("%appdata%//RhythmPy//Config//")
            )
            return str(WindowsAppDataConfig)
        elif Platform == "Linux" or Platform == "Darwin":
            LinuxAppdataConfig = str(os.path.expanduser("~/.RhythmPy/Config/"))
            return str(LinuxAppdataConfig)
        else:
            raise Exception
    except Exception:
        print("failed to get AppdataConfigDir")


# gets home dir + RhythmPy/Logs
def AppDataLogsDir():
    """Gets the folder where Log files are to be stored based on running OS"""
    try:
        Platform = platform.system()
        if Platform == "Windows":
            WindowsAppDataLogs = str(os.path.expandvars("%appdata%//RhythmPy//Logs//"))
            return str(WindowsAppDataLogs)
        elif Platform == "Linux" or Platform == "Darwin":
            LinuxAppdataLogs = str(os.path.expanduser("~/.RhythmPy/Logs/"))
            return str(LinuxAppdataLogs)
        else:
            raise Exception
    except Exception:
        print("failed to get AppDataLogsDir")
