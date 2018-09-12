print('FUNCTIONS LOADED')
import time
def initialStart():
    print('Initialising PyGame...')
    
    score = 0
    #import pygame
    #pygame.init()
    #print('Done!')

def printSystemInfo():
    import platform
    print("Running on "+ platform.platform() + ' ' + platform.machine() + ' on cpu ' + platform.processor())


def statCheck():
    print('Creating stats file...')
    createFile = open("stats.txt","w+")


def usercheck():
    print('UC')
    global username
    username = str(input("Welcome to Music Quiz! Please, enter your name (or 'stats' to view stats)"))
    global statfile
    statfile = open("stats.txt",'r')
    if username == 'stats':
            print("Pullin' up the stats...hold on a sec")
            statfile = open("stats.txt",'r')
            print(statFile)
    statfile.close()

    statfile = open("stats.txt","r")
    if(username in statfile):
        print("Sorry, that username is already taken...")
        time.sleep(2.5)
        game()
    else:
        global password
        password = input('Please enter a password (and keep it a secret!)')
        time.sleep(0.5)

def saveLoginInfo():
    statFile = open("stats.txt",'a')
    statFile.write(username + ',' + password + '\n')
