from getpass import getuser

import webbrowser
import importlib
import datetime
import shutil
import json
import time
import os

import Setup.FirstOpen
import Setup.Settings

import Backups
from BackupsCounter import BackupsCounter
from Vault import VaultEN
from VaultStats import VaultStatsEN
from Dwellers import DwellersEN

# Set the color palette
White = '\033[0m'
Cyan = '\033[96m'
Blue = '\033[94m'
Yellow = '\033[93m'
Green = '\033[92m'
Red = '\033[91m'

#Set variables
BackupsCount = []
BackupsCount.append(BackupsCounter)
date = datetime.date.today()

# Create a clear element
def clear(): # @note Clear ()
    os.system("cls")



# Create a backup element
def Backup(): # @note Backup ()
    BackupsCount.append(1)

    shutil.copyfile("./Files/Vault.Json", "./Backups/Backup-" + str(sum(BackupsCount)) + ".Json")



    with open ("./Scripts/BackupsCounter.py", "r") as file:
        fileData = file.read()

    fileData = fileData.replace('''BackupsCounter = ''' + str(sum(BackupsCount) - 1), '''BackupsCounter = ''' + str(sum(BackupsCount)))

    with open ("./Scripts/BackupsCounter.py", "w") as file:
        file.write(fileData)



    with open ("./Scripts/Backups.py", "r") as file:
        fileData = file.read()

    if sum(BackupsCount) - 1 == 0:
        fileData = fileData.replace('''# Last Backup''', '''    elif BackupsCounter.BackupsCounter > 0:
        print(Yellow + "[''' + str(sum(BackupsCount)) + '''] " + Green + "[''' + date.strftime("%m") + '''-''' + date.strftime("%d") + '''-''' + date.strftime("%y") + ''' ''' + time.strftime("%H:%M:%S") +'''] " + White + "[Backup-''' + str(sum(BackupsCount)) + '''.Json]" + White)
# Last Backup''')
    elif sum(BackupsCount) - 1 > 0:
        fileData = fileData.replace('''# Last Backup''', '''        print(Yellow + "[''' + str(sum(BackupsCount)) + '''] " + Green + "[''' + date.strftime("%m") + '''-''' + date.strftime("%d") + '''-''' + date.strftime("%y") + ''' ''' + time.strftime("%H:%M:%S") +'''] " + White + "[Backup-''' + str(sum(BackupsCount)) + '''.Json]" + White)
# Last Backup''')



    if sum(BackupsCount) - 1 == 0:
        fileData = fileData.replace('''# Last Recovery''', '''    print("")
    BackupToRecover = input(Yellow + "[Backup To Recover] ")

    if BackupToRecover == "1":
        if os.path.exists("./Files/Vault.Json"):
            os.remove("./Files/Vault.Json")
        shutil.copy("./Backups/Backup-1.Json", "./Files/Vault.Json")

        print("")
        print(Green + "The file has been recovered" + White)
        time.sleep(1)
# Last Recovery''')
    elif sum(BackupsCount) - 1 > 0:
        fileData = fileData.replace('''# Last Recovery''', '''    elif BackupToRecover == "''' + str(sum(BackupsCount)) + '''":
        if os.path.exists("./Files/Vault.Json"):
            os.remove("./Files/Vault.Json")
        shutil.copy("./Backups/Backup-''' + str(sum(BackupsCount)) + '''.Json", "./Files/Vault.Json")

        print("")
        print(Green + "The file has been recovered" + White)
        time.sleep(1)
# Last Recovery''')

    with open ("./Scripts/Backups.py", "w") as file:
        file.write(fileData)





# The basic program function
def Program(): # @note Program ()
    clear()

    if Setup.FirstOpen.FirstOpen == "True": # If not is the first time the program is open
        Backup()
        Engine()
    elif Setup.FirstOpen.FirstOpen == "False": # If is the first time the program is open
        print("                    @@@@@@@@@@                    ")
        print("              @@@@@@@%%%%%%%%@@@@@@@@             ")
        print("          @@@@@%%%%%%%%%%%%%%%%%%%%%@@@@@         ")
        print("       @@@@%%%%@@@@@@@@@@@.,,@@@@@@@%%%%@@@@      ")
        print("    @@@@%%%%%%@%%@@@...(....,,,,,,@%%%%%%%%@@@@   ")
        print("  @@@@%%%%%%@.@@@ .........,,,,,,,,,@@%%%%%%%@@@@ ")
        print(" @@@@%%%%%%%@.....@   /@   .@@,,,,,,,,,@%%%%%%@@@@")
        print("@@@@%%%%%%%@,@,#@           ........@,,,@%%%%%%@@@")
        print("@@@%%%%%%%%%%@              /......@,,,,@%%%%%%%@@")
        print("@@%%%%%%%%%%@   @            ......@.,,,@%%%%%%%@@")
        print("@@%%%%%%%%%@    @   @       @ .....&.&@@*%%%%%%%@@")
        print("@@%%%&@@@@@@      @@          ....@..@@&@@@@@%%%@@")
        print("@@@%%%%@@@@@             @    ........@@@@@@%%%%@@")
        print("@@@%%%%%@@@@& @ @@# .@@(   @ .........@@@@%%%%%@@@")
        print("@@@@%%%%%%@@@     @@@@@@     .....@@&@@@@%%%%%@@@@")
        print("  @@@@%%%%%@@@@     .      .....@@@@@@@@%%%%%@@@@ ")
        print("    @@@@%%%%%@@@@         ...@@#%%@@@@%%%%%@@@@   ")
        print("      @@@@%%%%@%%%%@@@@@@@%%%%%%%%%%@%%%@@@@      ")
        print("         @@@@@%%%%%%%%%%%%%%%%%%%%%%@@@@@         ")
        print("             @@@@@@@@%%%%%%%%@@@@@@@@             ")
        print("                    @@@@@@@@@@                    ")

        print("")

        print("This Software Was Coded By Fortuna")

        print("")

        print(Yellow + '[Enter "En" For English Translation]' + White)

        Language = input("" + Green)

        # If the language selected exists
        if Language.upper() == "EN":
            if os.path.exists("./Scripts/Setup/Settings.py"):
                os.remove("./Scripts/Setup/Settings.py")
            
            file = open("./Scripts/Setup/Settings.py", "w")
            file.write('Language = "' + Language + '"\n')
            file.write('KeyAccess = "Admin"')
            file.close()
        else: # If the language selected doesnt exist
            print(Red + "[Error] [That Is Not An Existing Language]" + White)

        print("")

        if Setup.Settings.Language.upper() == "DEFAULT": # If the language is Default
            print(Yellow + '[!] [Enter Access Key]' + White)
        elif Setup.Settings.Language.upper() == "EN": # Elif the language is English
            print(Yellow + '[!] [Enter Access Key]' + White)

        Key = input(Green)

        if Key.upper() == Setup.Settings.KeyAccess.upper(): # If the key is correct
        # Change the variable FirstOpen to "True"
            if os.path.exists("./Scripts/Setup/FirstOpen.py"):
                os.remove("./Scripts/Setup/FirstOpen.py")

            file = open("./Scripts/Setup/FirstOpen.py", "w")
            file.write('FirstOpen = "True"')
            file.close()

            Engine()
        else: # If the key is incorrect
            print(Red + "[Error] [Incorrect Access Key]" + White)

            # Set the variables of settings to the oringal ones
            if os.path.exists("./Scripts/Setup/Settings.py"):
                os.remove("./Scripts/Setup/Settings.py")
                
            file = open("./Scripts/Setup/Settings.py", "w")
            file.write('Language = "Default"\n')
            file.write('KeyAccess = "Admin"')
            file.close()

            print("")
    else: # If is an error with the program files
        print(Red + "[Error] [Execution Files Were Modified]" + White)



def Engine(): # @note Engine ()
    clear()

    if Setup.Settings.Language.upper() == "DEFAULT": # If language is Default
        print(Yellow + "[Backups] !Backups")
        print(Green + "Recover deleted files")

        print("")

        print(Yellow + "[Vault] !Vault")
        print(Green + "Basic shelter configuration")

        print("")

        print(Yellow + "[Vault Stats] !Vault-Stats")
        print(Green + "View and modify game statistics")

        print("")

        print(Yellow + "[Dwellers] !Dwellers")
        print(Green + "View and modify shelter workers")

        print("")

        print(Yellow + "[Support] !Support " + White + "[Bot Support]")
        print(Yellow + "[Credits] !Credits " + White + "[Contribution Credits]")
        print(Yellow + "[Exit] !Exit " + White + "[Exit Program]")

        print("")
        Command = input("Command > " + Green) # A input to set a command

        if Command.upper() == "!SUPPORT":
            webbrowser.open_new("https://fortuna561.github.io/Fallout-Shelter-Support/Index.html")
        elif Command.upper() == "!CREDITS":
            print(Yellow + "[Fortuna] " + White + "[Https://Github.Com/Fortuna561]")
            print(Yellow + "[Rakion99] " + White + "[Https://Github.Com/Rakion99]")
            time.sleep(5)
            Engine()
        elif Command.upper() == "!EXIT":
            if os.path.exists("./Files/Data.Json"):
                os.remove("./Files/Data.Json")

            if os.path.exists("./Files/Stats.Json"):
                os.remove("./Files/Stats.Json")
        elif Command.upper() == "!BACKUPS":
            importlib.reload(Backups)
            Backups.Backups()
            Engine()
        elif Command.upper() == "!VAULT":
            VaultEN()
            Engine()
        elif Command.upper() == "!VAULT-STATS":
            VaultStatsEN()
            Engine()
        elif Command.upper() == "!DWELLERS":
            DwellersEN()
            Engine()
        else:
            print("")
            print(Red + "[Error] [That command doesn't exist]" + White)
            time.sleep(1)
            Engine()
    elif Setup.Settings.Language.upper() == "EN": # Elif language is English
        print(Yellow + "[Backups] !Backups")
        print(Green + "Recover deleted files")

        print("")

        print(Yellow + "[Vault] !Vault")
        print(Green + "Basic shelter configuration")

        print("")

        print(Yellow + "[Vault Stats] !Vault-Stats")
        print(Green + "View and modify game statistics")

        print("")

        print(Yellow + "[Dwellers] !Dwellers")
        print(Green + "View and modify shelter workers")

        print("")

        print(Yellow + "[Support] !Support " + White + "[Bot Support]")
        print(Yellow + "[Credits] !Credits " + White + "[Contribution Credits]")
        print(Yellow + "[Exit] !Exit " + White + "[Exit Program]")

        print("")
        Command = input("Command > " + Green) # A input to set a command

        if Command.upper() == "!SUPPORT":
            webbrowser.open_new("https://fortuna561.github.io/Fallout-Shelter-Support/Index.html")
        elif Command.upper() == "!CREDITS":
            print(Yellow + "[Fortuna] " + White + "[Https://Github.Com/Fortuna561]")
            print(Yellow + "[Rakion99] " + White + "[Https://Github.Com/Rakion99]")
            time.sleep(5)
            Engine()
        elif Command.upper() == "!EXIT":
            if os.path.exists("./Files/Data.Json"):
                os.remove("./Files/Data.Json")

            if os.path.exists("./Files/Stats.Json"):
                os.remove("./Files/Stats.Json")
        elif Command.upper() == "!BACKUPS":
            importlib.reload(Backups)
            Backups.Backups()
            Engine()
        elif Command.upper() == "!VAULT":
            VaultEN()
            Engine()
        elif Command.upper() == "!VAULT-STATS":
            VaultStatsEN()
            Engine()
        elif Command.upper() == "!DWELLERS":
            DwellersEN()
            Engine()
        else:
            print("")
            print(Red + "[Error] [That command doesn't exist]" + White)
            time.sleep(1)
            Engine()

Program()