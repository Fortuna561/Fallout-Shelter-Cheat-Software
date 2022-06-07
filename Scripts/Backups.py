from getpass import getuser

import importlib
import shutil
import time
import os

import BackupsCounter

White = '\033[0m'
Cyan = '\033[96m'
Blue = '\033[94m'
Yellow = '\033[93m'
Green = '\033[92m'
Red = '\033[91m'

def clear(): # @note Clear ()
    os.system("cls")

def Backups(): # @note Backups()
    clear()

    importlib.reload(BackupsCounter)
    if BackupsCounter.BackupsCounter == 0:
        print(Red + "[Error] [You don't have backups]" + White)
        time.sleep(1)
# Last Backup

# Last Recovery