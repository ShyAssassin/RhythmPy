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
        cap = cv2.VideoCapture()
        cap.open(Stream)
        i = 0
        # tries to open stream 20 times
        while not cap.open() & i < 20:
            i = i + 1
            cap.open(Stream)
            time.sleep(1)
        if not cap.open:
            raise ("failed to open Stream")
        return cap

    def StartStream(self, FPS=60):
        """Starts FFmpeg Stream"""
        # fmt: off
        subprocess.run(
            [
                "ffmpeg",
                # The use of –probesize and –analyzeduration help FFMPEG to recognize the audio and video stream parameters of a file
                "-probesize", "1MB",
                # Resolution
                "-video_size", "1920x1080",
                # Framerate
                "-framerate", FPS,
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
            check=True,
        )
        # fmt: on

    def get_screenshot(self, Stream):
        ret, frame = Stream.read()
        return frame

    def start(self):
        """Starts Window Capture"""
        self.stopped = False
        t = Thread(target=self._run)
        t.start()

    def stop(self):
        """Stops Window Capture"""
        self.stopped = True

    def _run(self):
        self.StartStream()
        self.Stream = self.OpenStream()
        while not self.stopped:
            # get an updated image of the game
            screenshot = self.get_screenshot(Stream=self.Stream)
            # Lock the thread while updating the results
            self.lock.acquire()
            self.screenshot = screenshot
            self.lock.release()
