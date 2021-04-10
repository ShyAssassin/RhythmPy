import shutil

def CheckFFmpeg():
    """Checks if FFmpeg is installed on the system"""
    return shutil.which('ffmpeg') is not None
