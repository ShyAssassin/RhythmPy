from threading import Thread, Lock
import cv2
import time
import subprocess


class WindowCapture:

    # threading properties
    stopped = True
    lock = None
    screenshot = None

    def __init__(self, window_name=None):
        # create a thread lock object
        self.lock = Lock()

        # if no window name is given, capture the entire screen
        if window_name is None:
            pass
        else:
            pass

    def OpenStream(self, Stream="udp://127.0.0.1:1234/"):
        """Opens FFmpeg Stream"""
        try:
            self.cap = cv2.VideoCapture()
            self.cap.open(Stream)
        except Exception:
            i = 0
            # tries to open stream 20 times
            while not self.cap.open() & i < 20:
                i = i + 1
                self.cap.open(Stream)
                time.sleep(1)
            if not self.cap.open:
                raise ("failed to open Stream")
        return self.cap

    def CloseStream(self):
        """Closes FFmpeg Stream"""
        self.cap.release()

    def StartFFmpeg(self, FPS=60):
        """Starts FFmpeg Stream"""
        # fmt: off
        self.ffmpeg = subprocess.Popen(
            [
                "ffmpeg",
                # The use of –probesize and –analyzeduration helps FFmpeg to recognize the audio and video stream parameters of a file
                "-probesize", "1MB",
                # Resolution
                "-video_size", "1920x1080",
                # Framerate
                "-framerate", str(FPS),
                # (filter) Driver
                "-f", "x11grab",
                # Input device (Desktop)
                "-i", ":0.0",
                # Bitrate
                "-b:v", "2000k",
                # Quality factor
                "-crf", "0",
                # Compression rate
                "-preset", "ultrafast",
                # Encoder
                "-vcodec", "libx264",
                # (Filter) Stream with mpegts over udp
                "-f", "mpegts", "udp://127.0.0.1:1234",
            ],
        )
        # fmt: on

    def StopFFmpeg():
        pass

    def GetScreenshot(self, Stream):
        ret, frame = Stream.read()
        return frame

    def GetScreenSize(self):
        pass

    def start(self):
        """Starts Window Capture"""
        self.stopped = False
        self.thread = Thread(target=self._run, daemon=True)
        self.thread.name = "Window Capture"
        self.thread.start()

    def stop(self):
        """Stops Window Capture"""
        try:
            self.stopped = True
            self.CloseStream()
            self.ffmpeg.terminate()
            self.StopFFmpeg()
            self.thread.join()
        except Exception:
            raise (Exception)

    def _run(self):
        self.StartFFmpeg()
        self.Stream = self.OpenStream()
        while not self.stopped:
            # get an updated image of the game
            screenshot = self.GetScreenshot(Stream=self.Stream)
            # Lock the thread while updating the results
            self.lock.acquire()
            self.screenshot = screenshot
            self.lock.release()
