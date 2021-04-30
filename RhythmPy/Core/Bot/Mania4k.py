import platform

# fmt: off
# if we dont do this horibleness the logger will output
# multiple times
if "Logger" not in dir():
    global logger
    from Core.Logger import Logger
    loggerinit = Logger()
    logger = loggerinit.StartLogger(name=__name__)
import threading

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
        logger.warning('FFmpeg is not installed on current linux system')
        raise ModuleNotFoundError
# fmt: on


class Mania4k:
    def Start(self, Config, Running):
        try:
            self.thread = threading.Thread(target=self._run, args=(Config, Running))
            # Start the execution
            self.thread.start()
            logger.info("Started Thread for bot")
        except threading.ThreadError:
            logger.critical("Failed to start Thread for bot")
            logger.exception()

    def _run(self, Config, Running):
        self.Running = Running
        try:
            # will need to be updated to reflect the name of window found in Config
            self.Wincap = wincap.WindowCapture(None)
            self.Wincap.start()
            logger.info("Window Capture started!")
        except Exception:
            logger.exception("Failed to start Window capture\n")
            self.Running = False
        try:
            while True:
                # stops bot when Running is False
                if self.Running == False:
                    break
                # stops program from crashing on first frame of WinCap
                if self.Wincap.screenshot is None:
                    continue
                ScreenCap = self.Wincap.screenshot
        except Exception:
            logger.exception("Something went very wrong \n")

    def Stop(self):
        self.Running = False
        try:
            self.Wincap.stop()
            logger.info("Stopped WinCap")
        except Exception:
            logger.warning("Failed to stop WinCap")
        try:
            self.thread.join()
            logger.info("closed bots thread")
        except threading.ThreadError:
            logger.warning("Failed to close bots thread")
