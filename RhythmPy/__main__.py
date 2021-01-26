try:
    from .Modules import (
        CreateAppdataDir,
        FileManager,
    )
except ImportError:
    from Modules import (
        CreateAppdataDir,
        FileManager,
    )

try:
    from .Gui import GuiRun
    import Cli
except ImportError:
    from Gui import GuiRun
    import Cli

if __name__ == "__main__":
    Fm = FileManager()
    ConfigFile = Fm.LoadSettings()
    if ConfigFile["CliMode"] in [True, "True", "true"]:
        # runs cli version
        pass
    else:
        GuiRun()
