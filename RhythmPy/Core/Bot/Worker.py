import threading
from Core import FileManager
import ctypes
import numpy as np

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
        self.ThreadNumber = ThreadNumber
        self.Threadname = str("Worker " + str(ThreadNumber))
        # base Config
        self.BaseConfig = FileManager.LoadConfig(ConfigFile)

    def Start(self):
        """Starts the worker thread"""
        try:
            self.Running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.name = self.Threadname
            self.thread.start()
        except threading.ThreadError:
            logger.exception(
                "Failed to start worker thread number %s\n", self.ThreadNumber
            )
            raise threading.ThreadError

    def Stop(self):
        """Stops worker thread"""
        self.Running = False
        self.thread.join()

    def _run(self):
        global ScreenCap
        self.GetValues()
        while self.Running == True:
            if type(ScreenCap) == np.ndarray:
                (BGR) = ScreenCap[self.PosY, self.PosX]
                # so we dont check same frame twice
                ScreenCap = None

    def Update(self, address):
        """Updates workers current information using a memory address"""
        global ScreenCap  # using global because local doesnt work for some reason
        ScreenCap = ctypes.cast(address, ctypes.py_object).value

    def GetValues(self):
        # current Worker thread number will relate to what collum we are working on in order from 1 to n
        self.CollumConfig = self.BaseConfig[str("Collum " + str(self.ThreadNumber + 1))]
        # Key to be pressed
        self.Key = self.CollumConfig["Key"]
        # Postions
        self.PosX = int(self.CollumConfig["Position"]["X"])
        self.PosY = int(self.CollumConfig["Position"]["Y"])
        # note colours
        self.NotePrimaryColour = self.CollumConfig["Colours"]["Note Primary"]
        self.NoteSecondaryColour = self.CollumConfig["Colours"]["Note Secondary"]
        # slider colours
        self.SliderPrimaryColour = self.CollumConfig["Colours"]["Slider Primary"]
        self.SliderSecondaryColour = self.CollumConfig["Colours"]["Slider Secondary"]
