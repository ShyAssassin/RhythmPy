import subprocess
from Core.Logger import Logger


def BuildUpdater():
    """Used for building the Updater"""
    # start logger
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    try:
        logger.info("Building Updater...")
        Build = subprocess.run(
            ["cmake", "--build", "."],
            cwd=r"Updater/Build",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        # god only knows why stderr does not get asigned if we dont do this
        if Build.stderr != "":
            raise (Exception)
        logger.info("Updater built successfully")
    except Exception:
        for i in str(Build.stderr).replace(r"\n", "\n").split("\n"):
            if i in ["\n", "", " "]:
                pass
            else:
                logger.warning(i)
        logger.warning("Updater failed to build")
        raise ChildProcessError
