import threading
import ctypes
from Core import FileManager

# fmt: off
# if we dont do this horibleness the logger will output
# multiple times
if "Logger" not in dir():
    global logger
    from Core.Logger import Logger
    loggerinit = Logger()
    loggerinit.CreateLogFolder()
    logger = loggerinit.StartLogger(name=__name__)
# fmt: on


class Worker:
    def __init__(self, ThreadNumber, ConfigFile):
        self.ScreenCap = None
        self.Running = False
        self.Threadname = str("Worker " + str(ThreadNumber))
        self.Config = FileManager.LoadConfig(ConfigFile)

    def Update(self, address):
        """Updates workers current information using a memory address"""
        self.ScreenCap = ctypes.cast(address, ctypes.py_object).value

    def Start(self):
        """Starts the worker thread"""
        try:
            self.Running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.name = self.Threadname
            self.thread.start()
        except threading.ThreadError:
            logger.exception("Failed to start worker thread\n")
            raise Exception

    def _run(self):
        while self.Running == True and self.ScreenCap != None:
            # resets frame so we dont do the same frame twice
            self.ScreenCap = None

    def Stop(self):
        """Stops worker thread"""
        self.Running = False
        self.thread.join()
