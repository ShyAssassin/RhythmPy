import subprocess
from Core.Logger import Logger


def CreateBuildFolder():
    """Used for creating folder to hold cmake files"""
    # start logger
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    try:
        logger.info("Creating Build folder...")
        BuildFolder = subprocess.run(["mkdir", "-p", "Build"], cwd=r"Updater/")
        logger.info("Created Build Folder")
    except Exception:
        logger.warning(
            "Failed to create Build dir\n"
            + str(BuildFolder.stderr).replace(r"\n", "\n")
        )
        raise (Exception)
