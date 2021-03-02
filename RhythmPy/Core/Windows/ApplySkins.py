# from Core.Logger import Logger
import os
import sys
from os import path

class ApplySkins:
    class Osu:
        def __init__(self):
            self.OsuSkinDir = self.GetOsuSkinDir()
            self.CreateSkinDir(self.OsuSkinDir)
            self.WriteSkin(self.OsuSkinDir)

        def GetOsuSkinDir(self):
            try:
                AppDataLocal = str(os.path.expandvars("%localappdata%"))
                OsuDir = str(AppDataLocal + '//osu!')
                OsuSkinDir = str(OsuDir + '//Skins')
                return str(OsuSkinDir)
            except Exception:
                print("failed to get Osu Skin Dir")

        def CreateSkinDir(self, Dir):
            if path.exists(Dir + "/RhythmPy") == False:
                os.mkdir(Dir + "/RhythmPy")

        def WriteSkin(self, Dir):
            pass

    class Quaver:
        def __init__(self):
            pass

ApplySkins.Osu()