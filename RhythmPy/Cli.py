import os
import sys
import threading

from PIL import ImageTk

# more retarded imports
try:
    from .Modules import (
        CloseGlobal,
        CreateAppdataDir,
        FileManager,
        FirstRun,
        IsProcessRunning,
        Logger,
        WindowCapture,
    )
    from .Settings import Settings

    # from .SplashScreen import SplashScreen
except ImportError:
    from Modules import (
        CloseGlobal,
        CreateAppdataDir,
        FileManager,
        FirstRun,
        IsProcessRunning,
        Logger,
        WindowCapture,
    )
    from Settings import Settings


class CliRun:
    def __init__():
        print("soon")


if __name__ == "__main__":
    CliRun()
