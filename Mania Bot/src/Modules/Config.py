import json

# may i just say how much i DESPISE JSON
class ConfigRead:
    def __init__(self):
        global ConfigR
        try:
            self.Configdir = 'Config.json'
            self.ConfigOpen = open(self.Configdir, "r")
            ConfigR = json.loads(self.ConfigOpen.read())
        except:
            print('you should probably cry')

    def Debug(self):
        Debug = ConfigR["Debug"]
        return Debug

    def Version(self):
        Version = ConfigR["Version"]
        return Version

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
        global Configdir
        try:
            Configdir = 'Config.json'
            self.ConfigOpen = open(Configdir, "r")
            ConfigW = json.loads(self.ConfigOpen.read())
        except:
            print('cant find file')

    def Debug(self, Value):
        ConfigW["Debug"] = Value
        with open(Configdir, "w") as file:
            json.dump(ConfigW, file, indent=4)

    class Osu4K:
        def __init__(self):
            self.Config = ConfigW["Osu4K"]

    class Quaver4K:
        def __init__(self):
            self.Config = ConfigW["Quaver4K"]

# =======================================================================

ConfigWrite().Debug("kill me")