import subprocess
from Core.Logger import Logger
import os


def CreateBuildFolder():
    """Used for creating folder to hold cmake files"""
    # start logger
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    try:
        logger.info("Creating Build folder...")
        os.mkdir("Updater/Build")
        logger.info("Created Build Folder")
    except FileExistsError:
        logger.info("Build dir already exists")
    except PermissionError:
        logger.exception("Failed to create Build Dir")
