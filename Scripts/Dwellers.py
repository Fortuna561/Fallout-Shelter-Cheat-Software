from getpass import getuser

import collections
import json
import os

StatsCount = []
DwellerCount = []
DwellerChange = []

White = '\033[0m'
Cyan = '\033[96m'
Blue = '\033[94m'
Yellow = '\033[93m'
Green = '\033[92m'
Red = '\033[91m'

def clear(): # @note Clear ()
    os.system("cls")



def arrayToString(s): # @note ArrayToString()
    str1 = ""

    for ele in s: 
        str1 += ele  

    return str1 





def changeStatsEN(): # @note Change Stats()
    clear()

    StatsCount.clear()
    DwellerCount.clear()
    DwellerCount.append(1)

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for dwellers in data["dwellers"]:
            for dwellers2 in dwellers["dwellers"]:
                for i in range(len(dwellers2)):
                    if sum(DwellerChange) == sum(DwellerCount):
                        # Stats
                        for stats in dwellers2["stats"]:
                            for i in range(len(stats)):
                                Stats = str(dwellers2["stats"])

                                file = open("./Files/Stats.json", "w")
                                file.write(Stats)
                                file.close()

                                with open ("./Files/Stats.json", "r") as file:
                                    fileData = file.read()

                                fileData = fileData.replace("'", '"')

                                with open ("./Files/Stats.json", "w") as file:
                                    file.write(fileData)

                                with open("./Files/Stats.json") as file:
                                    data = json.load(file)
                                for stats in data["stats"]:
                                    for i in range(len(stats)):
                                        if sum(StatsCount) == 0:
                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 1:
                                            print(Yellow + "[S] " + White + str(stats["value"]))
                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 2:
                                            print(Yellow + "[P] " + White + str(stats["value"]))
                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 3:
                                            print(Yellow + "[E] " + White + str(stats["value"]))
                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 4:
                                            print(Yellow + "[C] " + White + str(stats["value"]))
                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 5:
                                            print(Yellow + "[I] " + White + str(stats["value"]))
                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 6:
                                            print(Yellow + "[A] " + White + str(stats["value"]))
                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 7:
                                            print(Yellow + "[L] " + White + str(stats["value"]))
                                            StatsCount.append(1)
                                            break

                                StatsCount.clear()
                                print("")

                                for stats in data["stats"]:
                                    for i in range(len(stats)):
                                        if sum(StatsCount) == 0:
                                            Value0 = str(stats["value"])
                                            Mod0 = str(stats["mod"])
                                            Exp0 = str(stats["exp"])
                                            HashKey0 = str(stats["$$hashKey"])

                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 1:
                                            OldValue1 = str(stats["value"])
                                            Mod1 = str(stats["mod"])
                                            Exp1 = str(stats["exp"])
                                            HashKey1 = str(stats["$$hashKey"])

                                            Value1 = input(Yellow + "[S] " + White)
                                            ValueArray1 = []

                                            if int(Value1) > 10:
                                                ValueArray1.clear()
                                                ValueArray1.append("10")
                                            else:
                                                ValueArray1.clear()
                                                ValueArray1.append(Value1)

                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 2:
                                            OldValue2 = str(stats["value"])
                                            Mod2 = str(stats["mod"])
                                            Exp2 = str(stats["exp"])
                                            HashKey2 = str(stats["$$hashKey"])

                                            Value2 = input(Yellow + "[P] " + White)
                                            ValueArray2 = []

                                            if int(Value2) > 10:
                                                ValueArray2.clear()
                                                ValueArray2.append("10")
                                            else:
                                                ValueArray2.clear()
                                                ValueArray2.append(Value2)

                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 3:
                                            OldValue3 = str(stats["value"])
                                            Mod3 = str(stats["mod"])
                                            Exp3 = str(stats["exp"])
                                            HashKey3 = str(stats["$$hashKey"])

                                            Value3 = input(Yellow + "[E] " + White)
                                            ValueArray3 = []

                                            if int(Value3) > 10:
                                                ValueArray3.clear()
                                                ValueArray3.append("10")
                                            else:
                                                ValueArray3.clear()
                                                ValueArray3.append(Value3)

                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 4:
                                            OldValue4 = str(stats["value"])
                                            Mod4 = str(stats["mod"])
                                            Exp4 = str(stats["exp"])
                                            HashKey4 = str(stats["$$hashKey"])

                                            Value4 = input(Yellow + "[C] " + White)
                                            ValueArray4 = []

                                            if int(Value4) > 10:
                                                ValueArray4.clear()
                                                ValueArray4.append("10")
                                            else:
                                                ValueArray4.clear()
                                                ValueArray4.append(Value4)

                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 5:
                                            OldValue5 = str(stats["value"])
                                            Mod5 = str(stats["mod"])
                                            Exp5 = str(stats["exp"])
                                            HashKey5 = str(stats["$$hashKey"])

                                            Value5 = input(Yellow + "[I] " + White)
                                            ValueArray5 = []

                                            if int(Value5) > 10:
                                                ValueArray5.clear()
                                                ValueArray5.append("10")
                                            else:
                                                ValueArray5.clear()
                                                ValueArray5.append(Value5)

                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 6:
                                            OldValue6 = str(stats["value"])
                                            Mod6 = str(stats["mod"])
                                            Exp6 = str(stats["exp"])
                                            HashKey6 = str(stats["$$hashKey"])

                                            Value6 = input(Yellow + "[A] " + White)
                                            ValueArray6 = []

                                            if int(Value6) > 10:
                                                ValueArray6.clear()
                                                ValueArray6.append("10")
                                            else:
                                                ValueArray6.clear()
                                                ValueArray6.append(Value6)

                                            StatsCount.append(1)
                                            break
                                        if sum(StatsCount) == 7:
                                            OldValue7 = str(stats["value"])
                                            Mod7 = str(stats["mod"])
                                            Exp7 = str(stats["exp"])
                                            HashKey7 = str(stats["$$hashKey"])

                                            Value7 = input(Yellow + "[L] " + White)
                                            ValueArray7 = []

                                            if int(Value7) > 10:
                                                ValueArray7.clear()
                                                ValueArray7.append("10")
                                            else:
                                                ValueArray7.clear()
                                                ValueArray7.append(Value7)

                                            StatsCount.append(1)
                                            break
                                break

                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) > sum(DwellerCount):
                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) < sum(DwellerCount):
                        break

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "stats": {
          "stats": [
            {
              "value": ''' + Value0 + ''',
              "mod": ''' + Mod0 + ''',
              "exp": ''' + Exp0 +''',
              "$$hashKey": "''' + HashKey0 +'''"
            },
            {
              "value": ''' + OldValue1 + ''',
              "mod": ''' + Mod1 + ''',
              "exp": ''' + Exp1 +''',
              "$$hashKey": "''' + HashKey1 +'''"
            },
            {
              "value": ''' + OldValue2 + ''',
              "mod": ''' + Mod2 + ''',
              "exp": ''' + Exp2 +''',
              "$$hashKey": "''' + HashKey2 +'''"
            },
            {
              "value": ''' + OldValue3 + ''',
              "mod": ''' + Mod3 + ''',
              "exp": ''' + Exp3 +''',
              "$$hashKey": "''' + HashKey3 +'''"
            },
            {
              "value": ''' + OldValue4 + ''',
              "mod": ''' + Mod4 + ''',
              "exp": ''' + Exp4 +''',
              "$$hashKey": "''' + HashKey4 +'''"
            },
            {
              "value": ''' + OldValue5 + ''',
              "mod": ''' + Mod5 + ''',
              "exp": ''' + Exp5 +''',
              "$$hashKey": "''' + HashKey5 +'''"
            },
            {
              "value": ''' + OldValue6 + ''',
              "mod": ''' + Mod6 + ''',
              "exp": ''' + Exp6 +''',
              "$$hashKey": "''' + HashKey6 +'''"
            },
            {
              "value": ''' + OldValue7 + ''',
              "mod": ''' + Mod7 + ''',
              "exp": ''' + Exp7 +''',
              "$$hashKey": "''' + HashKey7 +'''"
            }
          ]
        },''', '''        "stats": {
          "stats": [
            {
              "value": ''' + Value0 + ''',
              "mod": ''' + Mod0 + ''',
              "exp": ''' + Exp0 +''',
              "$$hashKey": "''' + HashKey0 +'''"
            },
            {
              "value": ''' + arrayToString(ValueArray1) + ''',
              "mod": ''' + Mod1 + ''',
              "exp": ''' + Exp1 +''',
              "$$hashKey": "''' + HashKey1 +'''"
            },
            {
              "value": ''' + arrayToString(ValueArray2) + ''',
              "mod": ''' + Mod2 + ''',
              "exp": ''' + Exp2 +''',
              "$$hashKey": "''' + HashKey2 +'''"
            },
            {
              "value": ''' + arrayToString(ValueArray3) + ''',
              "mod": ''' + Mod3 + ''',
              "exp": ''' + Exp3 +''',
              "$$hashKey": "''' + HashKey3 +'''"
            },
            {
              "value": ''' + arrayToString(ValueArray4) + ''',
              "mod": ''' + Mod4 + ''',
              "exp": ''' + Exp4 +''',
              "$$hashKey": "''' + HashKey4 +'''"
            },
            {
              "value": ''' + arrayToString(ValueArray5) + ''',
              "mod": ''' + Mod5 + ''',
              "exp": ''' + Exp5 +''',
              "$$hashKey": "''' + HashKey5 +'''"
            },
            {
              "value": ''' + arrayToString(ValueArray6) + ''',
              "mod": ''' + Mod6 + ''',
              "exp": ''' + Exp6 +''',
              "$$hashKey": "''' + HashKey6 +'''"
            },
            {
              "value": ''' + arrayToString(ValueArray7) + ''',
              "mod": ''' + Mod7 + ''',
              "exp": ''' + Exp7 +''',
              "$$hashKey": "''' + HashKey7 +'''"
            }
          ]
        },''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

        DwellerChange.clear()
        DwellerCount.clear()

        print("")
        print(Green + "The stats has been changed" + White)

def changeLevelEN(): # @note Change Level()
    clear()

    DwellerCount.clear()
    DwellerCount.append(1)

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for dwellers in data["dwellers"]:
            for dwellers2 in dwellers["dwellers"]:
                for i in range(len(dwellers2)):
                    if sum(DwellerChange) == sum(DwellerCount):
                        # Configuration

                        SerializeId = str(dwellers2["serializeId"])

                        PermaDeath = str(dwellers2["health"]["permaDeath"])
                        PermaDeathArray = []

                        if PermaDeath == "True":
                            PermaDeathArray.append("true")
                        elif PermaDeath == "False":
                            PermaDeathArray.append("false")

                        # Id

                        Name = str(dwellers2["name"])
                        LastName = str(dwellers2["lastName"])
                        Happiness = str(dwellers2["happiness"]["happinessValue"])

                        # Health

                        MaxHealth = str(dwellers2["health"]["maxHealth"])
                        Health = str(dwellers2["health"]["healthValue"])
                        Radiation = str(dwellers2["health"]["radiationValue"])

                        # Experience

                        print(Yellow + "[Level] " + White + str(dwellers2["experience"]["currentLevel"]))
                        print("")

                        Storage = str(dwellers2["experience"]["storage"])
                        Accum = str(dwellers2["experience"]["accum"])
                        WastelandExperience = str(dwellers2["experience"]["wastelandExperience"])

                        NeedLvUp = str(dwellers2["experience"]["needLvUp"])
                        NeedLvUpArray = []

                        if NeedLvUp == "True":
                            NeedLvUpArray.append("true")
                        elif NeedLvUp == "False":
                            NeedLvUpArray.append("false")

                        OldExperience = str(dwellers2["experience"]["experienceValue"])
                        OldLevel = str(dwellers2["experience"]["currentLevel"])

                        Level = input(Yellow + "[Level] " + White)
                        LevelArray = []

                        if int(Level) > 50:
                            LevelArray.clear()
                            LevelArray.append("50")
                        else:
                            LevelArray.clear()
                            LevelArray.append(Level)

                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) > sum(DwellerCount):
                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) < sum(DwellerCount):
                        break

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "serializeId": ''' + SerializeId + ''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + Health + ''',
          "radiationValue": ''' + Radiation + ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + OldLevel + ''',
          "maxHealth": ''' + MaxHealth + '''
        },
        "experience": {
          "experienceValue": ''' + OldExperience + ''',
          "currentLevel": ''' + OldLevel + ''',
          "storage": ''' + Storage + ''',
          "accum": ''' + Accum + ''',
          "needLvUp": ''' + arrayToString(NeedLvUpArray) +''',
          "wastelandExperience": ''' + WastelandExperience +'''
        },''', '''        "serializeId": ''' + SerializeId +''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + Health + ''',
          "radiationValue": ''' + Radiation + ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + arrayToString(LevelArray) + ''',
          "maxHealth": ''' + MaxHealth + '''
        },
        "experience": {
          "experienceValue": ''' + OldExperience + ''',
          "currentLevel": ''' + arrayToString(LevelArray) +''',
          "storage": ''' + Storage + ''',
          "accum": ''' + Accum +''',
          "needLvUp": ''' + arrayToString(NeedLvUpArray) +''',
          "wastelandExperience": ''' + WastelandExperience +'''
        },''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

        DwellerChange.clear()
        DwellerCount.clear()

        print("")
        print(Green + "The level has been changed" + White)

def changeHealthEN(): # @note Change Health()
    clear()

    DwellerCount.clear()
    DwellerCount.append(1)

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for dwellers in data["dwellers"]:
            for dwellers2 in dwellers["dwellers"]:
                for i in range(len(dwellers2)):
                    if sum(DwellerChange) == sum(DwellerCount):
                        # Configuration

                        SerializeId = str(dwellers2["serializeId"])
                        PermaDeath = str(dwellers2["health"]["permaDeath"])
                        PermaDeathArray = []

                        if PermaDeath == "True":
                            PermaDeathArray.append("true")
                        elif PermaDeath == "False":
                            PermaDeathArray.append("false")

                        # Id

                        Name = str(dwellers2["name"])
                        LastName = str(dwellers2["lastName"])
                        Happiness = str(dwellers2["happiness"]["happinessValue"])

                        # Health

                        print(Yellow + "[Max Health] " + White + str(dwellers2["health"]["maxHealth"]))
                        print(Yellow + "[Health] " + White + str(dwellers2["health"]["healthValue"]))
                        print("")

                        OldMaxHealth = str(dwellers2["health"]["maxHealth"])
                        OldHealth = str(dwellers2["health"]["healthValue"])
                        Radiation = str(dwellers2["health"]["radiationValue"])

                        MaxHealth = input(Yellow + "[Max Health] " + White)
                        MaxHealthArray = []

                        Health = input(Yellow + "[Health] " + White)
                        HealthArray = []

                        if int(MaxHealth) > 644:
                            MaxHealthArray.clear()
                            MaxHealthArray.append("644")
                        else:
                            MaxHealthArray.clear()
                            MaxHealthArray.append(MaxHealth)

                        if int(Health) > int(arrayToString(MaxHealthArray)):
                            HealthArray.clear()
                            HealthArray.append(arrayToString(MaxHealthArray))
                        else:
                            HealthArray.clear()
                            HealthArray.append(Health)

                        # Experience

                        Level = str(dwellers2["experience"]["currentLevel"])

                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) > sum(DwellerCount):
                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) < sum(DwellerCount):
                        break

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "serializeId": ''' + SerializeId + ''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + OldHealth + ''',
          "radiationValue": ''' + Radiation + ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + Level + ''',
          "maxHealth": ''' + OldMaxHealth + '''
        },''', '''        "serializeId": ''' + SerializeId +''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + arrayToString(HealthArray) + ''',
          "radiationValue": ''' + Radiation + ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + Level + ''',
          "maxHealth": ''' + arrayToString(MaxHealthArray) + '''
        },''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

        DwellerChange.clear()
        DwellerCount.clear()

        print("")
        print(Green + "The health has been changed" + White)

def changeHappinessEN(): # @note Change Happiness()
    clear()

    DwellerCount.clear()
    DwellerCount.append(1)

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for dwellers in data["dwellers"]:
            for dwellers2 in dwellers["dwellers"]:
                for i in range(len(dwellers2)):
                    if sum(DwellerChange) == sum(DwellerCount):
                        # Configuration

                        SerializeId = str(dwellers2["serializeId"])
                        PermaDeath = str(dwellers2["health"]["permaDeath"])
                        PermaDeathArray = []

                        if PermaDeath == "True":
                            PermaDeathArray.append("true")
                        elif PermaDeath == "False":
                            PermaDeathArray.append("false")

                        # Id

                        print(Yellow + "[Happiness] " + White + str(dwellers2["happiness"]["happinessValue"]))
                        print("")

                        Name = str(dwellers2["name"])
                        LastName = str(dwellers2["lastName"])
                        OldHappiness = str(dwellers2["happiness"]["happinessValue"])

                        Happiness = input(Yellow + "[Happiness] " + White)
                        HappinessArray = []

                        if int(Happiness) > 100:
                            HappinessArray.clear()
                            HappinessArray.append("100")
                        else:
                            HappinessArray.clear()
                            HappinessArray.append(Happiness)

                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) > sum(DwellerCount):
                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) < sum(DwellerCount):
                        break

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "serializeId": ''' + SerializeId + ''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + OldHappiness + '''
        }''', '''        "serializeId": ''' + SerializeId +''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        }''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

        DwellerChange.clear()
        DwellerCount.clear()

        print("")
        print(Green + "The happiness has been changed" + White)

def changeRadiationEN(): # @note Change Radiation()
    clear()

    DwellerCount.clear()
    DwellerCount.append(1)

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for dwellers in data["dwellers"]:
            for dwellers2 in dwellers["dwellers"]:
                for i in range(len(dwellers2)):
                    if sum(DwellerChange) == sum(DwellerCount):
                        # Configuration

                        SerializeId = str(dwellers2["serializeId"])
                        PermaDeath = str(dwellers2["health"]["permaDeath"])
                        PermaDeathArray = []

                        if PermaDeath == "True":
                            PermaDeathArray.append("true")
                        elif PermaDeath == "False":
                            PermaDeathArray.append("false")

                        # Id

                        Name = str(dwellers2["name"])
                        LastName = str(dwellers2["lastName"])
                        Happiness = str(dwellers2["happiness"]["happinessValue"])

                        # Health

                        print(Yellow + "[Radiation] " + White + str(dwellers2["health"]["radiationValue"]))
                        print("")

                        MaxHealth = str(dwellers2["health"]["maxHealth"])
                        Health = str(dwellers2["health"]["healthValue"])
                        OldRadiation = str(dwellers2["health"]["radiationValue"])

                        Radiation = input(Yellow + "[Radiation] " + White)
                        RadiationArray = []

                        if int(Radiation) > 100:
                            RadiationArray.clear()
                            RadiationArray.append("100")
                        else:
                            RadiationArray.clear()
                            RadiationArray.append(Radiation)

                        # Experience

                        Level = str(dwellers2["experience"]["currentLevel"])

                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) > sum(DwellerCount):
                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) < sum(DwellerCount):
                        break

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "serializeId": ''' + SerializeId + ''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + Health + ''',
          "radiationValue": ''' + OldRadiation + ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + Level + ''',
          "maxHealth": ''' + MaxHealth + '''
        },''', '''        "serializeId": ''' + SerializeId +''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + Health + ''',
          "radiationValue": ''' + arrayToString(RadiationArray)+ ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + Level + ''',
          "maxHealth": ''' + MaxHealth + '''
        },''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

        DwellerChange.clear()
        DwellerCount.clear()

        print("")
        print(Green + "The radiation has been changed" + White)

def changeEquipmentEN(): # @note Change Equipment()
    clear()

    StatsCount.clear()
    DwellerCount.clear()
    DwellerCount.append(1)

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for dwellers in data["dwellers"]:
            for dwellers2 in dwellers["dwellers"]:
                for i in range(len(dwellers2)):
                    if sum(DwellerChange) == sum(DwellerCount):
                        # Configuration

                        SavedRoom = str(dwellers2["savedRoom"])
                        LastChild = str(dwellers2["lastChildBorn"])
                        Rarity = str(dwellers2["rarity"])
                        DeathTime = str(dwellers2["deathTime"])
                        HashKey = str(dwellers2["$$hashKey"])

                        # Armor

                        print(Yellow + "[1] " + White + "Lab coat " + Yellow + "[I] " + Cyan + "[+3] " + Green + "[I: 3] " + White + "[Common]")
                        print(Yellow + "[2] " + White + "Lab coat advanced " + Yellow + "[I] " + Cyan + "[+5] " + Green + "[I: 5] " + Blue + "[Rare]")
                        print(Yellow + "[3] " + White + "Lab coat expert " + Yellow + "[I] " + Cyan + "[+7] " + Green + "[I: 7] " + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[4] " + White + "Battle armor " + Yellow + "[S] " + Cyan + "[+3] " + Green + "[S: 2] [E: 1]" + White + "[Common]")
                        print(Yellow + "[5] " + White + "Sturdy battle armor " + Yellow + "[S] " + Cyan + "[+5] " + Green + "[S: 3] [E: 2]" + Blue + "[Rare]")
                        print(Yellow + "[6] " + White + "Heavy battle armor " + Yellow + "[S] " + Cyan + "[+7] " + Green + "[S: 4] [E: 3]" + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[7] " + White + "Combat armor " + Yellow + "[S] " + Cyan + "[+3] " + Green + "[S: 2] [A: 1]" + White + "[Common]")
                        print(Yellow + "[8] " + White + "Sturdy combat armor " + Yellow + "[S] " + Cyan + "[+5] " + Green + "[S: 3] [A: 2]" + Blue + "[Rare]")
                        print(Yellow + "[9] " + White + "Heavy combat armor " + Yellow + "[S] " + Cyan + "[+7] " + Green + "[S: 4] [A: 3]" + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[10] " + White + "Leather armor " + Yellow + "[E] " + Cyan + "[+3] " + Green + "[S: 2] [E: 1]" + White + "[Common]")
                        print(Yellow + "[11] " + White + "Sturdy leather armor " + Yellow + "[E] " + Cyan + "[+5] " + Green + "[S: 3] [E: 2]" + Blue + "[Rare]")
                        print(Yellow + "[12] " + White + "Heavy leather armor " + Yellow + "[E] " + Cyan + "[+7] " + Green + "[S: 4] [E: 3]" + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[13] " + White + "Leather raider armor " + Yellow + "[A] " + Cyan + "[+3] " + Green + "[P: 2] [A: 1]" + White + "[Common]")
                        print(Yellow + "[14] " + White + "Sturdy raider armor " + Yellow + "[A] " + Cyan + "[+5] " + Green + "[P: 3] [A: 2]" + Blue + "[Rare]")
                        print(Yellow + "[15] " + White + "Heavy raider armor " + Yellow + "[A] " + Cyan + "[+7] " + Green + "[P: 4] [A: 3]" + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[16] " + White + "Sturdy metal armor " + Yellow + "[S] " + Cyan + "[+5] " + Green + "[S: 3] [L: 2]" + Blue + "[Rare]")
                        print(Yellow + "[17] " + White + "Heavy metal armor " + Yellow + "[S] " + Cyan + "[+7] " + Green + "[S: 4] [L: 3]" + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[18] " + White + "Wasteland medic " + Yellow + "[P] " + Cyan + "[+3] " + Green + "[P: 2] [L: 1]" + White + "[Common]")
                        print(Yellow + "[19] " + White + "Wasteland doctor " + Yellow + "[P] " + Cyan + "[+5] " + Green + "[P: 3] [L: 2]" + Blue + "[Rare]")
                        print(Yellow + "[20] " + White + "Wasteland surgeon " + Yellow + "[P] " + Cyan + "[+7] " + Green + "[P: 4] [L: 3]" + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[21] " + White + "Treasure hunter gear " + Yellow + "[S] " + Cyan + "[+3] " + Green + "[S: 2] [P: 1]" + White + "[Common]")
                        print(Yellow + "[22] " + White + "Bounty hunter gear " + Yellow + "[S] " + Cyan + "[+5] " + Green + "[S: 3] [P: 2]" + Blue + "[Rare]")
                        print(Yellow + "[23] " + White + "Mutant hunter gear " + Yellow + "[S] " + Cyan + "[+7] " + Green + "[S: 4] [P: 3]" + Yellow + "[Legendary]")

                        print("")

                        OldArmor = str(dwellers2["equipedOutfit"]["id"])
                        ArmorType = str(dwellers2["equipedOutfit"]["type"])

                        ArmorAsigned = str(dwellers2["equipedOutfit"]["hasBeenAssigned"])
                        ArmorAsignedArray = []

                        if ArmorAsigned == "True":
                            ArmorAsignedArray.append("true")
                        elif ArmorAsigned == "False":
                            ArmorAsignedArray.append("false")

                        RandomArmorAsigned = str(dwellers2["equipedOutfit"]["hasRandonWeaponBeenAssigned"])
                        RandomArmorAsignedArray = []

                        if RandomArmorAsigned == "True":
                            RandomArmorAsignedArray.append("true")
                        elif RandomArmorAsigned == "False":
                            RandomArmorAsignedArray.append("false")

                        Armor = input(Yellow + "[Armor] " + White)
                        ArmorArray = []

                        if Armor == "1":
                            ArmorArray.clear()
                            ArmorArray.append("LabCoat")
                        elif Armor == "2":
                            ArmorArray.clear()
                            ArmorArray.append("LabCoat_Advanced")
                        elif Armor == "3":
                            ArmorArray.clear()
                            ArmorArray.append("LabCoat_Expert")
                        elif Armor == "4":
                            ArmorArray.clear()
                            ArmorArray.append("BattleArmor")
                        elif Armor == "5":
                            ArmorArray.clear()
                            ArmorArray.append("BattleArmor_Sturdy")
                        elif Armor == "6":
                            ArmorArray.clear()
                            ArmorArray.append("BattleArmor_Heavy")
                        elif Armor == "7":
                            ArmorArray.clear()
                            ArmorArray.append("CombatArmor")
                        elif Armor == "8":
                            ArmorArray.clear()
                            ArmorArray.append("CombatArmor_Sturdy")
                        elif Armor == "9":
                            ArmorArray.clear()
                            ArmorArray.append("CombatArmor_Heavy")
                        elif Armor == "10":
                            ArmorArray.clear()
                            ArmorArray.append("WandererArmor")
                        elif Armor == "11":
                            ArmorArray.clear()
                            ArmorArray.append("WandererArmor_Sturdy")
                        elif Armor == "12":
                            ArmorArray.clear()
                            ArmorArray.append("WandererArmor_Heavy")
                        elif Armor == "13":
                            ArmorArray.clear()
                            ArmorArray.append("RaiderArmor")
                        elif Armor == "14":
                            ArmorArray.clear()
                            ArmorArray.append("RaiderArmor_Sturdy")
                        elif Armor == "15":
                            ArmorArray.clear()
                            ArmorArray.append("RaiderArmor_Heavy")
                        elif Armor == "16":
                            ArmorArray.clear()
                            ArmorArray.append("MetalArmor")
                        elif Armor == "17":
                            ArmorArray.clear()
                            ArmorArray.append("MetalArmor_Heavy")
                        elif Armor == "18":
                            ArmorArray.clear()
                            ArmorArray.append("WastelandSurgeon_Settler")
                        elif Armor == "19":
                            ArmorArray.clear()
                            ArmorArray.append("WastelandSurgeon_Doctor")
                        elif Armor == "20":
                            ArmorArray.clear()
                            ArmorArray.append("WastelandSurgeon")
                        elif Armor == "21":
                            ArmorArray.clear()
                            ArmorArray.append("HunterGear_Treasure")
                        elif Armor == "22":
                            ArmorArray.clear()
                            ArmorArray.append("HunterGear_Bounty")
                        elif Armor == "23":
                            ArmorArray.clear()
                            ArmorArray.append("HunterGear_Mutant")

                        # Weapon

                        clear()

                        print(Yellow + "[1] " + White + "Pool cue " + Yellow + "[A] " + Cyan + "[4] " + Green + "[0] " + "[8] " + Blue + "[Rare]")
                        print(Yellow + "[2] " + White + "Kitchen knife " + Yellow + "[P] " + Cyan + "[7] " + Green + "[3] " + "[11] " + Blue + "[Rare]")
                        print(Yellow + "[3] " + White + "Baseball bat " + Yellow + "[S] " + Cyan + "[10] " + Green + "[5] " + "[15] " + Blue + "[Rare]")
                        print(Yellow + "[4] " + White + "Butcher knife " + Yellow + "[L] " + Cyan + "[13] " + Green + "[8] " + "[18] " + Blue + "[Rare]")
                        print(Yellow + "[5] " + White + "Pickaxe " + Yellow + "[E] " + Cyan + "[16] " + Green + "[11] " + "[21] " + Blue + "[Rare]")
                        print(Yellow + "[6] " + White + "Fire hydrant bat " + Yellow + "[I] " + Cyan + "[25] " + Green + "[19] " + "[31] " + Yellow + "[Legendary]")
                        print(Yellow + "[7] " + White + "Relentless raider sword " + Yellow + "[S] " + Cyan + "[22] " + Green + "[16] " + "[28] " + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[8] " + White + "Rusty .32 pistol " + Yellow + "[A] " + Cyan + "[1] " + Green + "[1] " + "[1] " + White + "[Common]")
                        print(Yellow + "[9] " + White + ".32 pistol " + Yellow + "[A] " + Cyan + "[1.5] " + Green + "[1] " + "[2] " + White + "[Common]")
                        print(Yellow + "[10] " + White + "Enhanced .32 pistol " + Yellow + "[A] " + Cyan + "[2] " + Green + "[1] " + "[3] " + White + "[Common]")
                        print(Yellow + "[11] " + White + "Hardened .32 pistol " + Yellow + "[A] " + Cyan + "[2.5] " + Green + "[1] " + "[4] " + Blue + "[Rare]")
                        print(Yellow + "[12] " + White + "Armor piercing .32 pistol " + Yellow + "[A] " + Cyan + "[3] " + Green + "[1] " + "[5] " + Blue + "[Rare]")
                        print(Yellow + "[13] " + White + "Wild Bill's Sidearm " + Yellow + "[A] " + Cyan + "[3.5] " + Green + "[1] " + "[6] " + Yellow + "[Legendary]")

                        print("")

                        print(Yellow + "[14] " + White + "Rusty 10mm pistol " + Yellow + "[A] " + Cyan + "[2] " + Green + "[2] " + "[2] " + White + "[Common]")
                        print(Yellow + "[15] " + White + "10mm pistol " + Yellow + "[A] " + Cyan + "[2.5] " + Green + "[2] " + "[3] " + White + "[Common]")
                        print(Yellow + "[16] " + White + "Enhanced 10mm pistol " + Yellow + "[A] " + Cyan + "[3] " + Green + "[2] " + "[4] " + White + "[Common]")
                        print(Yellow + "[17] " + White + "Hardened 10mm pistol " + Yellow + "[A] " + Cyan + "[3.5] " + Green + "[2] " + "[5] " + Blue + "[Rare]")
                        print(Yellow + "[18] " + White + "Armor piercing 10mm pistol " + Yellow + "[A] " + Cyan + "[4] " + Green + "[2] " + "[6] " + Blue + "[Rare]")
                        print(Yellow + "[19] " + White + "Lone Wanderer " + Yellow + "[A] " + Cyan + "[4.5] " + Green + "[2] " + "[7] " + Yellow + "[Legendary]")

                        print("")

                        OldWeapon = str(dwellers2["equipedWeapon"]["id"])
                        WeaponType = str(dwellers2["equipedWeapon"]["type"])

                        WeaponAsigned = str(dwellers2["equipedWeapon"]["hasBeenAssigned"])
                        WeaponAsignedArray = []

                        if WeaponAsigned == "True":
                            WeaponAsignedArray.append("true")
                        elif WeaponAsigned == "False":
                            WeaponAsignedArray.append("false")

                        RandomWeaponAsigned = str(dwellers2["equipedWeapon"]["hasRandonWeaponBeenAssigned"])
                        RandomWeaponAsignedArray = []

                        if RandomWeaponAsigned == "True":
                            RandomWeaponAsignedArray.append("true")
                        elif RandomWeaponAsigned == "False":
                            RandomWeaponAsignedArray.append("false")

                        Weapon = input(Yellow + "[Weapon] " + White)
                        WeaponArray = []

                        if Weapon == "1":
                            WeaponArray.clear()
                            WeaponArray.append("Melee_PoolCue")
                        elif Weapon == "2":
                            WeaponArray.clear()
                            WeaponArray.append("Melee_KitchenKnife")
                        elif Weapon == "3":
                            WeaponArray.clear()
                            WeaponArray.append("Melee_BaseballBat")
                        elif Weapon == "4":
                            WeaponArray.clear()
                            WeaponArray.append("Melee_ButcherKnife")
                        elif Weapon == "5":
                            WeaponArray.clear()
                            WeaponArray.append("Melee_Pickaxe")
                        elif Weapon == "6":
                            WeaponArray.clear()
                            WeaponArray.append("Melee_FireHydrantBat")
                        elif Weapon == "7":
                            WeaponArray.clear()
                            WeaponArray.append("Melee_RelentlessRaiderSword")
                        elif Weapon == "8":
                            WeaponArray.clear()
                            WeaponArray.append("032Pistol_Rusty")
                        elif Weapon == "9":
                            WeaponArray.clear()
                            WeaponArray.append("032Pistol")
                        elif Weapon == "10":
                            WeaponArray.clear()
                            WeaponArray.append("032Pistol_Enhanced")
                        elif Weapon == "11":
                            WeaponArray.clear()
                            WeaponArray.append("032Pistol_Hardened")
                        elif Weapon == "12":
                            WeaponArray.clear()
                            WeaponArray.append("032Pistol_ArmorPiercing")
                        elif Weapon == "13":
                            WeaponArray.clear()
                            WeaponArray.append("032Pistol_WildBillsSidearm")
                        elif Weapon == "14":
                            WeaponArray.clear()
                            WeaponArray.append("Pistol_Rusty")
                        elif Weapon == "15":
                            WeaponArray.clear()
                            WeaponArray.append("Pistol")
                        elif Weapon == "16":
                            WeaponArray.clear()
                            WeaponArray.append("Pistol_Enhanced")
                        elif Weapon == "17":
                            WeaponArray.clear()
                            WeaponArray.append("Pistol_Hardened")
                        elif Weapon == "18":
                            WeaponArray.clear()
                            WeaponArray.append("Pistol_ArmorPiercing")
                        elif Weapon == "19":
                            WeaponArray.clear()
                            WeaponArray.append("Pistol_LoneWanderer")

                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) > sum(DwellerCount):
                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) < sum(DwellerCount):
                        break

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "equipedOutfit": {
          "id": "''' + OldArmor + '''",
          "type": "''' + ArmorType + '''",
          "hasBeenAssigned": ''' + arrayToString(ArmorAsignedArray) + ''',
          "hasRandonWeaponBeenAssigned": ''' + arrayToString(RandomArmorAsignedArray) + '''
        },
        "equipedWeapon": {
          "id": "''' + OldWeapon + '''",
          "type": "''' + WeaponType + '''",
          "hasBeenAssigned": ''' + arrayToString(WeaponAsignedArray) + ''',
          "hasRandonWeaponBeenAssigned": ''' + arrayToString(RandomWeaponAsignedArray) + '''
        },
        "savedRoom": ''' + SavedRoom + ''',
        "lastChildBorn": ''' + LastChild + ''',
        "rarity": "''' + Rarity + '''",
        "deathTime": ''' + DeathTime + ''',
        "$$hashKey": "''' + HashKey + '''"''', '''        "equipedOutfit": {
          "id": "''' + arrayToString(ArmorArray) + '''",
          "type": "''' + ArmorType + '''",
          "hasBeenAssigned": ''' + arrayToString(ArmorAsignedArray) + ''',
          "hasRandonWeaponBeenAssigned": ''' + arrayToString(RandomArmorAsignedArray) + '''
        },
        "equipedWeapon": {
          "id": "''' + arrayToString(WeaponArray) + '''",
          "type": "''' + WeaponType + '''",
          "hasBeenAssigned": ''' + arrayToString(WeaponAsignedArray) + ''',
          "hasRandonWeaponBeenAssigned": ''' + arrayToString(RandomWeaponAsignedArray) + '''
        },
        "savedRoom": ''' + SavedRoom + ''',
        "lastChildBorn": ''' + LastChild + ''',
        "rarity": "''' + Rarity + '''",
        "deathTime": ''' + DeathTime + ''',
        "$$hashKey": "''' + HashKey + '''"''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

        DwellerChange.clear()
        DwellerCount.clear()

        print("")
        print(Green + "The outfit and weapon has been changed" + White)

def healEN(): # @note Heal()
    clear()

    DwellerCount.clear()
    DwellerCount.append(1)

    with open("./Files/Data.json") as file:
        data = json.load(file)

        for dwellers in data["dwellers"]:
            for dwellers2 in dwellers["dwellers"]:
                for i in range(len(dwellers2)):
                    if sum(DwellerChange) == sum(DwellerCount):
                        # Configuration

                        SerializeId = str(dwellers2["serializeId"])
                        PermaDeath = str(dwellers2["health"]["permaDeath"])
                        PermaDeathArray = []

                        if PermaDeath == "True":
                            PermaDeathArray.append("true")
                        elif PermaDeath == "False":
                            PermaDeathArray.append("false")

                        # Id

                        Name = str(dwellers2["name"])
                        LastName = str(dwellers2["lastName"])
                        Happiness = str(dwellers2["happiness"]["happinessValue"])

                        # Health

                        MaxHealth = str(dwellers2["health"]["maxHealth"])
                        OldHealth = str(dwellers2["health"]["healthValue"])
                        Radiation = str(dwellers2["health"]["radiationValue"])

                        HealthArray = []

                        HealthArray.clear()
                        HealthArray.append(arrayToString(MaxHealth))

                        # Experience

                        Level = str(dwellers2["experience"]["currentLevel"])

                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) > sum(DwellerCount):
                        DwellerCount.append(1)
                        break
                    elif sum(DwellerChange) < sum(DwellerCount):
                        break

        with open ("./Files/Vault.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace('''        "serializeId": ''' + SerializeId + ''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + OldHealth + ''',
          "radiationValue": ''' + Radiation + ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + Level + ''',
          "maxHealth": ''' + MaxHealth + '''
        },''', '''        "serializeId": ''' + SerializeId +''',
        "name": "''' + Name + '''",
        "lastName": "''' + LastName + '''",
        "happiness": {
          "happinessValue": ''' + Happiness + '''
        },
        "health": {
          "healthValue": ''' + arrayToString(HealthArray) + ''',
          "radiationValue": ''' + Radiation + ''',
          "permaDeath": ''' + arrayToString(PermaDeathArray) + ''',
          "lastLevelUpdated": ''' + Level + ''',
          "maxHealth": ''' + MaxHealth + '''
        },''')

        with open ("./Files/Vault.json", "w") as file:
            file.write(fileData)

        DwellerChange.clear()
        DwellerCount.clear()

        print("")
        print(Green + "The worker has been healed" + White)





def DwellersEN(): # @note Dwellers()
    clear()

    with open("./Files/Vault.json") as file: #@note Create Needs.Json
        data = json.load(file)

        if os.path.exists("./Files/Data.json"):
            os.remove("./Files/Data.json")

        file = open("./Files/Data.json", "w")
        file.write('{"dwellers": [' + str(data["dwellers"]) + "]}")
        file.close

        with open("./Files/Data.json", "r") as file:
            fileData = file.read()

        fileData = fileData.replace("'", '"')

        fileData = fileData.replace("True", "true")
        fileData = fileData.replace("False", "false")

        fileData = fileData.replace("None", '"None"')

        with open("./Files/Data.json", "w") as file:
            file.write(fileData)

    with open("./Files/Vault.json", "r") as file:
        collectionData = file.read()

    with open("./Files/Data.json") as file:
        data = json.load(file)

    for dwellers in data["dwellers"]:
        for dwellers2 in dwellers["dwellers"]:
            for i in range(len(dwellers2)):
                if collections.Counter(collectionData.split())['"happiness":'] >= 1:
                    DwellerCount.append(1)
                    print(Yellow + "[" + str(sum(DwellerCount)) + "] " + White + str(dwellers2["name"]) + " " + str(dwellers2["lastName"]))
                    break

    DwellerModifie = input("Option: ")

    if int(DwellerModifie) <= sum(DwellerCount):
        clear()

        DwellerChange.clear()
        DwellerChange.append(int(DwellerModifie))

        print(Yellow + "[1] " + White + "Change Stats Of Dweller")
        print(Yellow + "[2] " + White + "Change Level Of Dweller")
        print(Yellow + "[3] " + White + "Change Health Of Dweller")
        print(Yellow + "[4] " + White + "Change Happiness Of Dweller")
        print(Yellow + "[5] " + White + "Change Radiation On Dweller")
        print(Yellow + "[6] " + White + "Change Outfit And Weapon Of Dweller")
        print(Yellow + "[7] " + White + "Heal Dweller")

        Command = input("Option: ")

        if Command == "1":
            changeStatsEN() # @note Change Stats
        if Command == "2":
            changeLevelEN() # @note Change Level
        if Command == "3":
            changeHealthEN() # @note Change Health
        if Command == "4":
            changeHappinessEN() # @note Change Happiness
        if Command == "5":
            changeRadiationEN() # @note Change Radiation
        if Command == "6":
            changeEquipmentEN() # @note Change Equipment
        if Command == "7":
            healEN() # @note Heal