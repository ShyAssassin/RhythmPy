import os

try:
    os.system('pip install -r requirements.txt')
    print('all dependencies have been installed!\n press ENTER to exit')
    input()
    exit()
except:
    print('something went wrong \n press ENTER to exit')
    input()
    exit()
else:
    exit()