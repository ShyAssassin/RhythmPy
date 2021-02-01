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
    from .Cli import CliRun
except ImportError:
    from Gui import GuiRun
    from Cli import CliRun

if __name__ == "__main__":
    Fm = FileManager()
    ConfigFile = Fm.LoadSettings()
    try:
        if ConfigFile["CliMode"] in [True, "True", "true"]:
            CliRun()
        else:
            GuiRun()
    except Exception:
        GuiRun()
