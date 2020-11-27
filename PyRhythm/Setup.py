import ctypes
import enum
import subprocess
import sys
import os

'''
i honestly do not know how this even runs
but it does so i am not gonna complain
'''

class SW(enum.IntEnum):
    HIDE = 0
    MAXIMIZE = 3
    MINIMIZE = 6
    RESTORE = 9
    SHOW = 5
    SHOWDEFAULT = 10
    SHOWMAXIMIZED = 3
    SHOWMINIMIZED = 2
    SHOWMINNOACTIVE = 7
    SHOWNA = 8
    SHOWNOACTIVATE = 4
    SHOWNORMAL = 1


class ERROR(enum.IntEnum):
    ZERO = 0
    FILE_NOT_FOUND = 2
    PATH_NOT_FOUND = 3
    BAD_FORMAT = 11
    ACCESS_DENIED = 5
    ASSOC_INCOMPLETE = 27
    DDE_BUSY = 30
    DDE_FAIL = 29
    DDE_TIMEOUT = 28
    DLL_NOT_FOUND = 32
    NO_ASSOC = 31
    OOM = 8
    SHARE = 26

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def get_path():
    try:
        path = sys.executable
        path = path.replace('\python.exe', '')
        path = str(path)
        return path
    except:
        print('failed to cd into dir')

def bootstrap():
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
       # noinspection SpellCheckingInspection
        hinstance = ctypes.windll.shell32.ShellExecuteW(
            None,
            'runas',
            sys.executable,
            subprocess.list2cmdline(sys.argv),
            None,
            SW.SHOWNORMAL
        )
        if hinstance <= 32:
            raise RuntimeError(ERROR(hinstance))


def main():
    global ScriptDir
    path = get_path()
    print(path)
    print('if you are using ANACONDA or MiniConda please enter the environment name\nIf not, please press ENTER')
    print("Example: " + "PyRhythm")
    environment = input()
    if environment == None or environment == '' or environment =='no' or environment == 'N' or environment == 'n' or environment == ' ':
        print('installing to defualt python3')
    else:
        try:
            subprocess.run(['conda', 'activate', environment], check=True, shell=True)
            print('conda activated')
        except subprocess.CalledProcessError:
            subprocess.run(["cls"], shell=True)
            try:
                print('conda is not in your %PATH%')
                print('please input the full path of the anacondaa installation point\nDO NOT include the path of the environment you are wanting to use')
                print("Example: " + r"C:\Users\NAME\anaconda3")
                environment_path = input(r"")

                # cd's into given path
                try:
                    with cd(environment_path):
                        # just to test
                        subprocess.run(["dir"], shell=True, check=True)
                    # sets the correct dir
                    ScriptDir ="".join((environment_path, r"\Scripts"))
                    # clears console
                    subprocess.run(["cls"], shell=True)                
                except:
                    print('failed to cd into given path\npress ENTER to exit')
                    input()
                    exit()

                # cd's into Scripts
                try:
                    with cd(environment_path):
                        subprocess.run(["cd", ScriptDir], shell=True, check=True)
                except:
                    print('failed to cd into Scripts path\npress ENTER to exit')
                    input()
                    exit()

                # trys to activate conda
                try:
                    with cd(ScriptDir):
                        subprocess.run(["conda", "activate", environment], check=True, shell=True)
                except subprocess.CalledProcessError:
                    print('failed to activate conda Please install requirements manually\npress ENTER to exit')
                    input()
                    exit()
            except:
                print('something went wrong :(')
                input()
                exit()

    # installs the requirements
    try:
        try:
            if environment != None or environment != '' or environment != ' ':
                subprocess.run(['conda', 'activate', environment], check=True, shell=True)
                subprocess.run(["pip3", "install", "-r", "requirements.txt"], shell=True, check=True)
                print('dependincies have been installed, moving on to pywin32')
            else:
                subprocess.run(["pip3", "install", "-r", "requirements.txt"], shell=True, check=True)
                print('dependincies have been installed, moving on to pywin32')
        except subprocess.CalledProcessError:
            print('something went wrong\n install manually with dependincies manually with\n`pip -r requirements.txt`')
    except subprocess.CalledProcessError:
        print('Could not locate requirements.txt please make sure you are running this script from within the requirements folder\npress ENTER to exit')
        input()
        exit()

    # installs py win32
    try:
        with cd(path):
            subprocess.run(["dir"], shell=True, check=True)
            subprocess.run(["cls"], shell=True)
            subprocess.run(["python3", "pywin32_postinstall"], shell=True)
            print('everything has been installed! you can now close the window')
            input()
            exit()
    except:
        print('pywin32 system install failed\nthis is not needed you can continue ')
        input()
        exit()

if __name__ == "__main__":
    bootstrap()