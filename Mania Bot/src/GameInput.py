# pylint throws a fit when i import DirectInput normally
from .DirectInput import keyDown, keyUp

'''
we need this so we can check rgb values in parallel to other tasks 
and im to scared to edit the DirectInput code to add this feature so we do it here
and the only reason i am using oo is because it makes setting keys and colours easier and more efficient 
'''

class GameInput:
    def __init__(self, Key, Input, Colours):
        self.Key = Key
        self.Input = Input
        self.Colours = Colours

    def run(self):
        while self.Input in self.Colours:
            keyDown(self.Key)
            if self.Input not in self.Colours:
                keyUp(self.Key)