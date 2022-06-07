from getpass import getuser

import json
import os

White = '\033[0m'
Cyan = '\033[96m'
Blue = '\033[94m'
Yellow = '\033[93m'
Green = '\033[92m'
Red = '\033[91m'

def clear(): # @note Clear ()
    os.system("cls")





def changeNukasEN(): # @note Change Nukas()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Nuka] " + White + str(item["Nuka"]))
                    print("")

                    OldNuka = str(item["Nuka"])
                    Nuka = input(Yellow + "[Nuka] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "Nuka": ''' + OldNuka, '''        "Nuka": ''' + Nuka)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeNukaColasEN(): # @note Change Nuka Colas()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Nuka Cola] " + White + str(item["NukaColaQuantum"]))
                    print("")

                    OldNukaCola = str(item["NukaColaQuantum"])
                    NukaCola = input(Yellow + "[Nuka Cola] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "NukaColaQuantum": ''' + OldNukaCola, '''        "NukaColaQuantum": ''' + NukaCola)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeEnergyEN(): # @note Change Energy()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Energy] " + White + str(item["Energy"]))
                    print("")

                    OldEnergy = str(item["Energy"])
                    Energy = input(Yellow + "[Energy] " + White + str(item["Energy"]))

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "Energy": ''' + OldEnergy, '''        "Energy": ''' + Energy)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeWaterEN(): # @note Change Water()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Water] " + White + str(item["Water"]))
                    print("")

                    OldWater = str(item["Water"])
                    Water = input(Yellow + "[Water] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "Water": ''' + OldWater, '''        "Water": ''' + Water)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeFoodEN(): # @note Change Food()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Food] " + White + str(item["Food"]))
                    print("")

                    OldFood = str(item["Food"])
                    Food = input(Yellow + "[Food] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "Food": ''' + OldFood, '''        "Food": ''' + Food)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changePetCarrierEN(): # @note Change Pet Carrier()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Pet Carrier] " + White + str(item["PetCarrier"]))
                    print("")

                    OldPetCarrier = str(item["PetCarrier"])
                    PetCarrier = input(Yellow + "[Pet Carrier] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "PetCarrier": ''' + OldPetCarrier, '''        "PetCarrier": ''' + PetCarrier)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeLunchBoxEN(): # @note Change Lunch Box()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Lunch Box] " + White + str(item["LunchBox"]))
                    print("")

                    OldLunchBox = str(item["LunchBox"])
                    LunchBox = input(Yellow + "[Lunch Box] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "LunchBox": ''' + OldLunchBox, '''        "LunchBox": ''' + LunchBox)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeMrHandyEN(): # @note Change Mr Handy()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Mr Handy] " + White + str(item["MrHandy"]))
                    print("")

                    OldMrHandy = str(item["MrHandy"])
                    MrHandy = input(Yellow + "[Mr Handy] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "MrHandy": ''' + OldMrHandy, '''        "MrHandy": ''' + MrHandy)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeRadAwayEN(): # @note Change Rad Away()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Rad Away] " + White + str(item["RadAway"]))
                    print("")

                    OldRadAway = str(item["RadAway"])
                    RadAway = input(Yellow + "[Rad Away] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "RadAway": ''' + OldRadAway, '''        "RadAway": ''' + RadAway)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

def changeStimPackEN(): # @note Change Stim Pack()
    clear()

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for storage in data["vault"]:
            for resources in storage["storage"]:
                for item in resources["resources"]:
                    print(Yellow + "[Stim Pack] " + White + str(item["StimPack"]))
                    print("")

                    OldStimPack = str(item["StimPack"])
                    StimPack = input(Yellow + "[Stim Pack] " + White)

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "StimPack": ''' + OldStimPack, '''        "StimPack": ''' + StimPack)

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)






def VaultStatsEN(): # @note Vault Stats()
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

    print(Yellow + "[1] " + White +  "Change Nukas")
    print(Yellow + "[2] " + White +  "Change NukaColas")
    print(Yellow + "[3] " + White +  "Change Energy")
    print(Yellow + "[4] " + White +  "Change Water")
    print(Yellow + "[5] " + White +  "Change Food")
    print(Yellow + "[6] " + White +  "Change Pet Carrier")
    print(Yellow + "[7] " + White +  "Change Lunch Box")
    print(Yellow + "[8] " + White +  "Change Mr Handy")
    print(Yellow + "[9] " + White +  "Change Rad Away")
    print(Yellow + "[10] " + White +  "Change Stim Pack")
    print("")

    Command = input("Command > ")

    if Command == "1": # @note Change Nukas
        changeNukasEN()
    if Command == "2": # @note Change Nuka Colas
        changeNukaColasEN()
    if Command == "3": # @note Change Energy
        changeEnergyEN()
    if Command == "4": # @note Change Water
        changeWaterEN()
    if Command == "5": # @note Change Food
        changeFoodEN()
    if Command == "6": # @note Change Pet Carrier
        changePetCarrierEN()
    if Command == "7": # @note Change Lunch Box
        changeLunchBoxEN()
    if Command == "8": # @note Change Mr Handy
        changeMrHandyEN()
    if Command == "9": # @note Change Rad Away
        changeRadAwayEN()
    if Command == "10": # @note Change StimPack
        changeStimPackEN()