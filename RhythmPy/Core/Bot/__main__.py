from Core import FileManager
import threading
import platform
from .Worker import Worker

# fmt: off
# if we dont do this horibleness the logger will output
# multiple times
if "Logger" not in dir():
    global logger
    from Core.Logger import Logger
    loggerinit = Logger()
    loggerinit.CreateLogFolder()
    logger = loggerinit.StartLogger(name=__name__)

# checks platform and imports need winCap
platform = platform.system()
if platform == "Windows":
    from Core import Windows
    wincap = Windows
elif platform == "Linux" or platform == "Darwin":
    from Core import Linux
    # checks if ffmpeg is insttalled
    if Linux.CheckFFmpeg():
        wincap = Linux
    else:
        # will deal with this later!
        logger.warning('FFmpeg is not installed on current linux system exiting')
        raise ModuleNotFoundError
# fmt: on


class Bot:
    """used for utilizing the bot and its commands

    Args:
        Running, Bool: the current state of the bot
        ConfigFile, String: the location of a .json config file
    """

    def __init__(self, Running, ConfigFile):
        self.Running = Running
        self.ConfigFile = ConfigFile

    def __del__(self):
        pass

    def Start(self):
        """Starts the bot"""
        try:
            self.thread = threading.Thread(
                target=self._run, args=(self.ConfigFile,), daemon=True
            )
            self.thread.name = "Bot"
            self.thread.start()
            logger.info("Started bots thread")
        except threading.ThreadError:
            logger.exception("Failed to start bots thread\n")
            raise ("BotThreadingError")

    def _initialize(self, ConfigFile):
        """initializes the bot"""
        try:
            # loads config file
            try:
                self.Config = FileManager.LoadConfig(ConfigFile)
                logger.info("Loaded config file")
            except Exception:
                logger.exception("Failed to load config file\n")
                raise Exception
            # starts Window Capture and loads config file
            try:
                self.Wincap = wincap.WindowCapture(None)
                self.Wincap.start()
                logger.info("Window Capture started")
            except Exception:
                logger.exception("Failed to start Wincap\n")
                raise Exception
            # creates a list of worker threads for later use
            try:
                self.WorkerThreads = []
                for i in range(int(self.Config["Collums"])):
                    self.WorkerThreads.append(
                        Worker(ThreadNumber=i, ConfigFile=ConfigFile)
                    )
                logger.info("Created worker thread list")
            except Exception:
                logger.exception("failed to create list of worker threads\n")
                raise Exception
            # starts the worker threads
            try:
                for worker in self.WorkerThreads:
                    worker.Update(address=id(self.Wincap.screenshot))
                logger.info("Started worker threads")
            except Exception:
                logger.exception("Failed to start worker threads\n")
                raise Exception
        except Exception:
            logger.critical("Failed to initialize bot")
            self.Running = False
            raise Exception

    def _run(self, ConfigFile):
        self._initialize(ConfigFile)
        # starts worker threads
        for worker in self.WorkerThreads:
            worker.Start()
        while self.Running:
            for worker in self.WorkerThreads:
                worker.Update(address=id(self.Wincap.screenshot))

    def Stop(self):
        """Stops the bot"""
        try:
            self.Running = False
            # stops all worker threads
            try:
                for worker in self.WorkerThreads:
                    worker.Stop()
                logger.info("Stopped all worker threads")
                # clears / resets worker thread list
                self.WorkerThreads = []
            except Exception:
                logger.exception("Failed to stop worker threads")
                raise Exception
            # stops window capture
            try:
                self.Wincap.stop()
                logger.info("Stopped window capture")
            except Exception:
                logger.exception("Failed to stop Window Capture\n")
            # joins bots thread
            try:
                self.thread.join()
                logger.info("Closed bots thread")
            except Exception:
                logger.exception("Failed to close bots thread\n")
        except Exception:
            logger.critical("Failed to stop bot\n")
