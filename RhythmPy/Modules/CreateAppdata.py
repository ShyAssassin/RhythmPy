from os import path
import os


# creates dir for storing logs and configs in %appdata%/RhythmPy
def CreateAppdataDir():
    if path.exists(os.path.expandvars("%appdata%//RhythmPy")) == False:
        os.mkdir(os.path.expandvars("%appdata%//RhythmPy"))