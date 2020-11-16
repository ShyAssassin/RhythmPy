import subprocess
import os
import sys
import time
'''
used for compiling Mania Bot into a windows exe with pyinstaller
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
    print("Example: " + "Mania-Bot")
    environment = input()
    if environment == None or environment == '' or environment =='no' or environment == 'N' or environment == 'n' or environment == ' ':
        print('using defualt python3')
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
                print("something went wrong :'(")
                input()
                exit()

    try:
        print('please give the path of the mania bot dir')
        print('Example: ' + r'C:\Users\Assassin\Documents\GitHub\Mania-Bot\Mania Bot')
        maniaDIR = input()
        if environment != None or environment != '' or environment != ' ':
            with cd(maniaDIR):
                    subprocess.run(['conda', 'activate', environment, '&&', 'pyinstaller', '--onedir', '--debug=all', 'Main.spec', 'Main.py'], shell=True)
                    print('done building')
                    print('if there is no dist folder or the exe does not work make SURE that you have pyinstaller and Visual C++ Redistributable installed')
                    print('link to Visual C++ Redistributable download if needed:\nhttps://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads')
                    input()
                    exit()
        else:
            with cd(maniaDIR):
                subprocess.run(['pyinstaller', '--onedir', '--debug=all', 'Main.spec', 'Main.py'], shell=True)
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