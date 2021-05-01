import subprocess
from Core.Logger import Logger


def RunCmake():
    """Runs Cmake and creates build files"""
    # start logger
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    try:
        logger.info("Running Cmake...")
        Cmake = subprocess.run(
            ["cmake", "..", "-G", "Unix Makefiles"],
            cwd=r"Updater/Build",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        # god only knows why stderr does not get asigned if we dont do this
        if Cmake.stderr != "":
            raise (Exception)
        else:
            logger.info(
                "Cmake ran successfully\n" + str(Cmake.stdout).replace(r"\n", "\n")
            )
    except Exception:
        logger.warning("failed to run cmake\n" + str(Cmake.stderr).replace(r"\n", "\n"))
        raise (Exception)
