import json
import library

Game = input('osu or Quaver \n')
if Game == 'osu':
    Mode = input('4k or 7k \n')
    if Mode in ('4k', '4K', '4'):
        print('4k has been selected \n')
        # runs 4k
    else:
        print('7k has been selected \n')\
        # runs 7k
elif Game == 'quaver':
    Mode = input('4k or 7k \n')
    if Mode in ('4k', '4K', '4'):
        print('4k has been selected \n')
        # runs 4k
    else:
        print('7k has been selected \n')
        # runs 7k


