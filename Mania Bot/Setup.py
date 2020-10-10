import os

try:
    os.system('pip3 install -r requirements.txt')
    print('all dependencies have been installed!\n press ENTER to exit')
    input()
    exit
except:
    print('something went wrong')
    input()
    exit()
