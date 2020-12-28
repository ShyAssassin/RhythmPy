from os import path
import os


def CreateAppdataDir():
    if path.exists(os.path.expandvars("%appdata%//RhythmPy")) == False:
        os.mkdir(os.path.expandvars("%appdata%//RhythmPy"))