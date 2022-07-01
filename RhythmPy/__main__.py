# imports
try:
    # fmt: off
    import platform
    import traceback
    # Starts Logger
    try:
        from Core import FileManager
        from Core.Logger import Logger
        # creates appdata dir
        FileManager.CreateAppdataDir()
        logger = Logger()
        # creates log folder
        logger.CreateLogFolder()
        logger = logger.StartLogger(name=__name__)
    except (ImportError, ModuleNotFoundError):
        print("failed to start logger\n", traceback.format_exc())
        input()
        exit()

    # Splash Screen
    try:
        from Core.Gui import SplashScreen
        # starts splash screen
        splash = SplashScreen()
        splash.Start()
    except (ImportError, ModuleNotFoundError):
        logger.exception("failed to start splash screen\n")
        splash = None

    # if debug is enabled will attempt to build the updater
    from Core.Debug import Updater
    try:
        Settings = FileManager.LoadSettings()
        if Settings["Debug"] in [True, "True", "true"]:
            logger.info("Debug enabled attempting to build Updater")
            # checks if Rhythmpy is compiled
            if Updater.IsProduction() == False:
                Updater.CreateBuildFolder()
                Updater.RunCmake()
                Updater.BuildUpdater()
                Updater.CopyUpdater()
            else:
                logger.info("RhythmPy is being run in production skipping build...")
        else:
            logger.info('Debug not enabled skipping Updater build')
    except Exception:
        logger.warning("Settings.json missing skipping build")

    # creates needed files
    try:
        FileManager.CreateConfigFolder()
        FileManager.CreateConfigFiles()
        FileManager.CreatePluginFolder()
    except (ImportError, ModuleNotFoundError):
        logger.exception("Failed to create needed files\n")

    # imports the actual bot
    try:
        from Core import (
            FirstRun,
            Gui,
            Cli,
        )
    except (ImportError, ModuleNotFoundError):
        logger.exception("failed to import the bot\n")
        exit()
    # fmt: on
except Exception as e:
    print(e)
    input()
    exit()

if __name__ == "__main__":
    # gets current running system
    platform = platform.system()
    ConfigFile = FileManager.LoadSettings()

    # first run stuff
    try:
        if ConfigFile["FirstRun"] in [True, "True", "true"]:
            FirstRun().Run()
        else:
            logger.info("has been run before carrying on")
    except Exception:
        logger.warning("failed to apply skins\n")

    # starts the bot
    try:
        splash.Stop()
        if ConfigFile["CliMode"] in [True, "True", "true"]:
            Cli.Run()
        else:
            Gui.Run()
    except Exception:
        Gui.Run()
    except Exception:
        logger.exception("failed to start RhythmPy\n")
