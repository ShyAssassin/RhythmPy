from os import path
import os
import platform
from .Paths import AppDataDir, AppDataConfigDir


def CreateAppdataDir():
    """Creates dir for storing logs and configs in (%appdata%/RhythmPy) or (~//RhythmPy)"""
    Platform = platform.system()
    if Platform == "Windows":
        if path.exists(os.path.expandvars("%appdata%//RhythmPy")) == False:
            os.mkdir(os.path.expandvars("%appdata%//RhythmPy"))
    elif Platform == "Linux" or Platform == "Darwin":
        if path.exists(os.path.expanduser("~//RhythmPy")) == False:
            os.mkdir(os.path.expanduser("~//RhythmPy"))
