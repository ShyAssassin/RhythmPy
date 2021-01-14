import subprocess
import os
import sys
import time

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


class Build:
    def __init__(self):
        self.Type = None

    # asks for Build type
    def askBuild(self):
        while self.Type not in ["Dev", "dev", "Normal", "normal"]:
            if self.Type in ["Quit", "quit"]:
                sys.exit()

            if self.Type in ["Help", "help"]:
                print("the Dev build includes a console on runtime with --debug modes enabled while pyinstaller is Building the exe. The dev build is for well developers")
                print("Normal build does not include a console on runtime and only consists of the GUI. Normal mode is for just creating a exe that will work\n")

            self.Type = input("Normal or Dev Build?\nType Help for more info or quit to quit\n")

    def Build(self):
        print("you have selected %s build is this right?\nY/N" % (self.Type))
        # asks if the current mode is correct
        if input() in ["Y", "y", "Yes", "yes"]:
            print("Starting Build...")
            # checks if pyinstaller is installed
            try:
                subprocess.run(["pyinstaller", "-h"], check=True)
            except subprocess.CalledProcessError:
                print('Pyinstaller is not installed please')
                print('install it with: pip install pyinsaller')
                sys.exit()

            # clears console
            try:
                subprocess.run(['clear'], check=True)
            except subprocess.CalledProcessError:
                subprocess.run(['cls'], check=True)
            except:
                pass

            if self.Type in ["Dev", "dev"]:
                with cd(r"RhythmPy"):
                    try:
                        subprocess.run(["pyinstaller", "--onedir", "__main__Dev.spec", "__main__.py"], check=True)
                    except subprocess.CalledProcessError:
                        print('failed to create exe refer to /build log file')
                        sys.exit()
            elif self.Type in ["Normal", "normal"]:
                with cd(r"RhythmPy"):
                    try:
                        subprocess.run(['pyinstaller', '--onedir', '__main__.spec', '__main__.py'], check=True)
                    except subprocess.CalledProcessError:
                        print('failed to create exe refer to /build log file')
                        sys.exit()
        else:
            self.Type = None
            self.askBuild()



if __name__ == "__main__":
    build = Build()
    build.askBuild()
    build.Build()