if __name__ == "__main__":
    # fmt: off
    # creates appdata dir and needed files
    from Core import FileManager
    from Core.Logger import Logger
    try:
        FileManager.CreateAppdataDir()
        logger = Logger()
        logger.CreateLogFolder()
        FileManager.CreateConfigFolder()
        FileManager.CreateConfigFiles()
        FileManager.CreatePluginFolder()
        logger = logger.StartLogger(name=__name__)
    except Exception as e:
        print("i dont know and i dont want to know\n")
        print(e)
    # fmt: on

    # Imports
    try:
        from Core import Windows, FirstRun
        from Gui import GuiRun
        from Cli import CliRun
        import platform
    except ImportError:
        logger.exception("Failed to import needed libraries\n")

    # loads normal stuff
    try:
        ConfigFile = FileManager.LoadSettings()
        platform = platform.system()
    except Exception:
        logger.exception("oh no\n")

    # first run stuff
    try:
        try:
            if ConfigFile["FirstRun"] in [True, "True", "true"]:
                FirstRun().Run()
                if platform == "Windows":
                    Windows.ApplySkins.Osu()
                    # Windows.ApplySkins.Quaver()
                elif platform == "Linux" or platform == "Darwin":
                    pass
            else:
                logger.info("has been run before carrying on")
        except Exception:
            FirstRun().Run()
    except Exception:
        logger.warning("failed to apply skins\n")

    # bot stuff
    try:
        if ConfigFile["CliMode"] in [True, "True", "true"]:
            CliRun()
        else:
            GuiRun()
    except Exception:
        GuiRun()
    except Exception:
        logger.exception("failed to start RhythmPy\n")
