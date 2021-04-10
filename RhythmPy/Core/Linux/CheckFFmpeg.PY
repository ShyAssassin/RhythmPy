import shutil

def CheckFFmpeg():
    """checks if FFmpeg is installed on the system"""
    return shutil.which('ffmpeg') is not None
