import time
import random
import os
from os import path
from functions import *

initialStart()
def game():
    #Check if the stats file exists
    if path.exists('stats.txt') == False:
        print('Preparing for first time setup...')
        printSystemInfo()
        statCheck()
game()
#Check user info
usercheck()
saveLoginInfo()
