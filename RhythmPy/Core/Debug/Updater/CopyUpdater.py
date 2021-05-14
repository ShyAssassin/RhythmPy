from Core.Logger import Logger
import shutil
import platform


def CopyUpdater():
    """Copys Updater from build folder to root dir"""
    # start logger
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    try:
        logger.info("Copying Updater...")
        if platform.system() == "Windows":
            shutil.copy(r"Updater/Build/Updater.exe", "Updater.exe")
        else:
            shutil.copy(r"Updater/Build/Updater", "Updater.exe")
        logger.info("Coppied Updater from `Updater/Build/Updater`")
    except Exception:
        logger.exception("Failed to copy Updater\n")
        raise (Exception)
