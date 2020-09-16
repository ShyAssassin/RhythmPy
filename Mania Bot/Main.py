import json
import library
import threading
import logging

Game = input('osu or Quaver \n')
if Game == 'osu':
    Mode = input('4k or 7k \n')
    if Mode in ('4k', '4K', '4'):
        # runs 4k
        print('4k has been selected \n')
        
    else:
        # runs 7k
        print('7k has been selected \n')\
        
elif Game == 'quaver':
    Mode = input('4k or 7k \n')
    if Mode in ('4k', '4K', '4'):
        # runs 4k
        print('4k has been selected \n')
        
    else:
       # runs 7k 
       print('7k has been selected \n')
        