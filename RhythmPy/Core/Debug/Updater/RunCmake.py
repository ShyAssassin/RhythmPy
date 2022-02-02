import subprocess
from Core.Logger import Logger


def RunCmake():
    """Runs Cmake and creates build files"""
    # start logger
    logger = Logger()
    logger = logger.StartLogger(name=__name__)
    try:
        logger.info("Running Cmake...")
        try:
            # UNIX / Linux
            Cmake = subprocess.run(
                ["cmake", "..", "-G", "Unix Makefiles"],
                cwd=r"Updater/Build",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                check=True,
            )
        except Exception:
            # Windows
            Cmake = subprocess.run(
                ["cmake", "..", "-G", "MinGW Makefiles"],
                cwd=r"Updater/Build",
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
        # god only knows why stderr does not get asigned if we dont do this
        if Cmake.stderr != "":
            raise ReferenceError
        else:
            # logs formatted output
            for i in str(Cmake.stdout).replace(r"\n", "\n").split("\n"):
                # checks for endline
                if i in ["\n", "", " "]:
                    pass
                else:
                    logger.info(i)
            logger.info("Cmake ran successfully")
    except Exception:
        for i in str(Cmake.stderr).replace(r"\n", "\n").split("\n"):
            if i in ["\n", "", " "]:
                pass
            else:
                logger.warning(i)
        logger.warning("failed to run cmake")
        raise ChildProcessError
