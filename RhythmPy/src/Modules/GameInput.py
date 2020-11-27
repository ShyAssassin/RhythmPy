import os
import sys

# pylint throws a fit when i import DirectInput normally
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
try:
    from DirectInput import keyDown, keyUp
except:
    from .DirectInput import keyDown, keyUp

'''
we need this so we can check rgb values in parallel to other tasks 
and im to scared to edit the DirectInput code to add this feature so we do it here
and the only reason i am using oo is because it makes setting keys and colours easier and more efficient 
'''

class GameInput:
    def __init__(self, key, Input, Colours):
        self.Key = key
        self.Input = Input
        self.Colours = Colours

    def run(self):
        while self.Input in self.Colours:
            keyUp(self.Key)
            if self.Input not in self.Colours:
                keyDown(self.Key)
