# from Core.Logger import Logger
# import os
# import sys
# from os import path
# from tkinter import filedialog


# class ApplySkins:
#     """Puts required skins into relevant folders"""

#     class Osu:
#         def __init__(self):
#             self.logger = Logger()
#             self.logger = self.logger.StartLogger(name=__name__)
#             # gets the defualt osu skin path for windows
#             self.OsuSkinDir = str(self.GetOsuSkinDir())
#             if self.CreateSkinDir(str(self.OsuSkinDir)):
#                 self.WriteSkin(str(self.OsuSkinDir))

#         def GetOsuSkinDir(self):
#             try:
#                 AppDataLocal = str(os.path.expandvars("%localappdata%"))
#                 OsuDir = str(AppDataLocal + "//osu!")
#                 OsuSkinDir = str(OsuDir + "//Skins")
#                 if path.exists(OsuSkinDir) == False:
#                     raise Exception
#                 else:
#                     return str(OsuSkinDir)
#             except Exception:
#                 self.logger.exception("failed to get Osu Skin Dir\n")

#         def CreateSkinDir(self, Dir):
#             try:
#                 if path.exists(str(Dir + "//RhythmPy")) == False:
#                     os.mkdir(str(Dir + "//RhythmPy"))
#                     return True
#                 else:
#                     return False
#             except Exception:
#                 self.logger.exception("Failed to Create Osu Skin folder")

#         def WriteSkin(self, Dir):
#             try:
#                 RhythmPySkinDir = str(Dir + "//RhythmPy//PlaceHolder.txt")
#                 f = open(RhythmPySkinDir, "x")
#                 f.close()
#             except Exception:
#                 self.logger.exception("Failed to Write Osu skin")

#     class Quaver:
#         def __init__(self):
#             pass


# ApplySkins.Osu()
