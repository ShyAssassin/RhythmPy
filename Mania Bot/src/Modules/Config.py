import json

# may i just say how much i DESPISE JSON
class ConfigRead:
    def __init__(self):
        global ConfigR
        try:
            Configdir = 'Config.json'
            ConfigOpen = open(Configdir, "r")
            ConfigR = json.loads(ConfigOpen.read())
        except:
            print('you should probably cry')

    def Version(self):
        print(ConfigR["Version"])

    # Osu4K config
    class Osu4K:
        def __init__(self):
            self.Config = ConfigR['Osu4K']

        def WindowName(self):
            WindowName = self.Config["Window Name"]
            if WindowName == "" or WindowName == None or WindowName == " ":
                return None
            else:
                return WindowName
        
        def Collum1Pos(self):
            Collum1Pos = self.Config["Collum1Pos"]
            return Collum1Pos

        def Collum2Pos(self):
            Collum2Pos = self.Config["Collum2Pos"]
            return Collum2Pos

        def Collum3Pos(self):
            Collum3Pos = self.Config["Collum3Pos"]
            return Collum3Pos

        def Collum4Pos(self):
            Collum4Pos = self.Config["Collum4Pos"]
            return Collum4Pos
    # ================================================================

    # Quaver4k Config
    class Quaver4K:
        def __init__(self):
            self.Config = ConfigR['Quaver4K']
        
        def WindowName(self):
            WindowName = self.Config["Window Name"]
            if WindowName == "" or WindowName == None or WindowName == " ":
                return None
            else:
                return WindowName
        
        def Collum1Pos(self):
            Collum1Pos = self.Config["Collum1Pos"]
            return Collum1Pos

        def Collum2Pos(self):
            Collum2Pos = self.Config["Collum2Pos"]
            return Collum2Pos

        def Collum3Pos(self):
            Collum3Pos = self.Config["Collum3Pos"]
            return Collum3Pos

        def Collum4Pos(self):
            Collum4Pos = self.Config["Collum4Pos"]
            return Collum4Pos
    # ==================================================================
# ======================================================================

class ConfigWrite:
    def __init__(self):
        global ConfigW
        try:
            Configdir = 'Config.json'
            ConfigOpen = open(Configdir, "r")
            ConfigW = json.loads(ConfigOpen.read())
        except:
            print('if this dont work something is very wrong')

    class Osu4K:
        def __init__(self):
            self.Config = ConfigW["Osu4K"]

    class Quaver4K:
        def __init__(self):
            self.Config = ConfigW["Quaver4K"]
# =======================================================================


print(ConfigRead().Osu4K().WindowName())