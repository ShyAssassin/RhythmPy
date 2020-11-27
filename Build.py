import subprocess
import os
import sys
import time
'''
used for compiling PyRhythm into a windows exe with pyinstaller
will work on mac / linux later
'''
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

def Build():
    global ScriptDir
    path = get_path()
    print(path)
    print('if you are using ANACONDA or MiniConda please enter the environment name\nIf not, please press ENTER')
    print('I RECOMEND YOU USE A NEW AND DIFFERENT VIRTUAL ENVIROMENT WITH REQUIREMENTS INSTALLED TO BUILD!')
    print("Example: " + "PyRhythm")
    environment = input()

    try:
        print('please give the path of the PyRhythm dir')
        print('Example: ' + r'C:\Users\Assassin\Documents\GitHub\PyRhythm\PyRhythm')
        maniaDIR = input()
        if environment != None or environment != '' or environment != ' ':
            with cd(maniaDIR):
                    subprocess.run(['conda', 'activate', environment, '&&', 'pyinstaller', '--onedir', '--debug=all', 'Main.spec', 'Main.py'], shell=True, check=True)
                    print('done building')
                    print('if there is no dist folder or the exe does not work make SURE that you have pyinstaller and Visual C++ Redistributable installed')
                    print('link to Visual C++ Redistributable download if needed:\nhttps://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads')
                    input()
                    exit()
        else:
            with cd(maniaDIR):
                subprocess.run(['pyinstaller', '--onedir', '--debug=all', 'Main.spec', 'Main.py'], shell=True, check=True)
                print('done building')
                print('if there is no dist folder or the exe does not work make SURE that you have pyinstaller and Visual C++ Redistributable installed')
                print('link to Visual C++ Redistributable download if needed:\nhttps://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads')
                input()
                exit()
                    
    except:
        print('are you sure you have pyinstaller and Visual C++ Redistributable installed?')
        print('link to Visual C++ Redistributable download if needed:\nhttps://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads')
        input()
        exit()


if __name__ == "__main__":
    Build()