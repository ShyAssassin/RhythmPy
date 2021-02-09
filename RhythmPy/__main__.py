from Modules import FileManager


from Gui import GuiRun
from Cli import CliRun


if __name__ == "__main__":
    try:
        ConfigFile = FileManager.LoadSettings()
        if ConfigFile["CliMode"] in [True, "True", "true"]:
            CliRun()
        else:
            GuiRun()
    except Exception:
        GuiRun()
