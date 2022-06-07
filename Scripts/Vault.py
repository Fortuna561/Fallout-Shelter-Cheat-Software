from getpass import getuser

import json
import time
import os

White = '\033[0m'
Cyan = '\033[96m'
Blue = '\033[94m'
Yellow = '\033[93m'
Green = '\033[92m'
Red = '\033[91m'

def clear(): # @note Clear ()
    os.system("cls")





def changeVaultNameEN(): # @note Change Vault Name()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Vault Name] " + White + str(storage["VaultName"]))
                    print("")

                    OldVaultName = str(storage["VaultName"])
                    VaultName = input(Yellow + "[Vault Name] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''    "VaultName": "''' + OldVaultName + '''"''', '''    "VaultName": "''' + VaultName + '''"''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)





def VaultEN(): # @note Vault()
    clear()

    with open("./Files/Vault.json") as file: # @note Create Needs.Json
        data = json.load(file)

        if os.path.exists("./Files/Data.json"):
            os.remove("./Files/Data.json")

        file = open("./Files/Data.json", "w")
        file.write('{"vault": [' + str(data["vault"]) + "]}")
        file.close

        with open("./Files/Data.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace("'", '"')

        fileData = fileData.replace("True", "true")
        fileData = fileData.replace("False", "false")

        fileData = fileData.replace('], "storage": {"resources": {', '], "storage": [{"resources": [{')

        fileData = fileData.replace('}, "bonus": {"Nuka": 0, "Food": 0, "Energy": 0, "Water": 0, "StimPack": 0, "RadAway": 0, "Lunchbox": 0, "MrHandy": 0, "PetCarrier": 0, "CraftedOutfit": 0, "CraftedWeapon": 0, "NukaColaQuantum": 0, "CraftedTheme": 0}}, "inventory":', '}]}], "bonus": {"Nuka": 0, "Food": 0, "Energy": 0, "Water": 0, "StimPack": 0, "RadAway": 0, "Lunchbox": 0, "MrHandy": 0, "PetCarrier": 0, "CraftedOutfit": 0, "CraftedWeapon": 0, "NukaColaQuantum": 0, "CraftedTheme": 0}, "inventory":')

        with open("./Files/Data.json", "w") as file:
            file.write(fileData)

    print(Yellow + "[1] " + White + "Change Vault Name")

    Command = input("Command > ")

    if Command == "1": # @note Change Vault Name
        changeVaultNameEN()