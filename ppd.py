import os
import sys
import json
import datetime

script_path = os.path.abspath(sys.argv[0])

parent_directory = (os.path.dirname(script_path))

jsonfile = (rf"{str(parent_directory)}\safe_data.json")

tagep = False
tageudatump = False
datump = False
lango = "ENG"
sauswahl = None
tagejn = None
auswahl = None
start = None
tage = None
ppd = None
listename = None
neustart = None
ziel = None
tagedone = None
addvarnam = None
addvarz = None
DE = None
Eng = None
while True:
    while True:
        today = datetime.datetime.now()

        todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')

        if not os.path.exists(rf"{str(parent_directory)}\safe_data.json"):
            lang_new = input("which language would you like to use? press d/de/ger for german and e/eng for english  : ").lower()
            if lang_new == "d":
                DE = True
            elif lang_new == "de":
                DE = True
            elif lang_new == "ger":
                DE = True
            elif lang_new == "e":
                Eng = True
            elif lang_new == "eng":
                Eng = True
            if DE == True:
                file = open("safe_data.json", "a")
                file.write("{\n")
                file.write(f'\"lang": "DE"\n')
                file.write("}")
                file.close()
                lango = "DE"
            elif Eng == True:
                file = open("safe_data.json", "a")
                file.write("{\n")
                file.write(f'\"lang": "ENG"\n')
                file.write("}")
                file.close()
                lango = "ENG"
            else:
                print("please only type d/de/ger or e/eng")
                break

        else:
            file = open("safe_data.json", "r")
            jsonlesen = file.read()
            file.close()
            jsonlesbar = jsonlesen.replace("\n", "")
            jsoncmd = json.loads(jsonlesbar)
            lango = jsoncmd["lang"]

        liste = False
        if lango == "DE":
            print("wenn du stoppen willst drücke zu dem zeitpunkt x und wenn du irgendwann neustarten willst drücke n")
            sauswahl = input("willst du deín ergebnis speichern? JA/Nein :").lower()
        elif lango == "ENG":
            print("if you want to stop the program use (x) / if you want to restart use (n)")
            sauswahl = input("do you want to safe your result? yes/no :").lower()

        if sauswahl == "x":
            if lango == "DE":
                print("abgebrochen")
                input("sicher?")
            elif lango == "ENG":
                print("stopped")
                input("are you sure ?")
            exit()
        elif sauswahl == "n":
            if lango == "DE":
                print("neustart")
            elif lango == "ENG":
                print("restarting")
            pass
        elif sauswahl == "ja":
            liste = True
        elif sauswahl == "yes":
            liste = True

        if liste == True:
            if lango == "DE":
                tagejn = input("möchtest du dass die anzahl der tage in der liste genannt werden (t) oder das datum (d) oder beides (td)").lower()
            elif lango == "ENG":
                tagejn = input(
                    "Do you want the number of days in the list to be mentioned (t), the date (d), or both (td)?").lower()

            if tagejn == "td":
                tageudatump = True
            elif tagejn == "dt":
                tageudatump = True
            elif tagejn == "d":
                datump = True
            else:
                tagep = True
        else:
            liste = False

        if lango == "DE":
            auswahl = input(
                "drücke z zum ziel berechnen oder b zum berechnen vom endergebnis oder t für eine anzahl an tagen oder a für variablen : ").lower()

        elif lango == "ENG":
            auswahl = input(
                "Press z for calculating the target, or b for calculating the final result, or t for a number of days, or a for variables: ").lower()

        if auswahl == "x":
            if lango == "DE":
                print("abgebrochen")
                input("sicher?")
            elif lango == "ENG":
                print("Canceled")
                input("Are you sure?")
            exit()
        elif auswahl == "n":
            if lango == "DE":
                print("neustart")
            elif lango == "ENG":
                print("restarting")
            pass
        elif auswahl == "b":
            if lango == "DE":
                print("du bist im berechnen bereich")
                start = input("start angeben : ")

                tage = input("tage eingeben : ")

                ppd = input("prozent pro tag eingeben : ")
            elif lango == "ENG":
                print("You are in the calculation area")
                start = input("Enter the start amount: ")
                tage = input("Enter the number of days: ")
                ppd = input("Enter your percentage per day: ")

            if start == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif start == "n":
                if lango == "DE":
                    print("neustart")
                elif lango == "ENG":
                    print("restarting")
                pass
            elif tage == "n":
                if lango == "DE":
                    print("neustart")
                elif lango == "ENG":
                    print("restarting")
                pass
            elif tage == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif ppd == "n":
                if lango == "DE":
                    print("neustart")
                elif lango == "ENG":
                    print("restarting")
                pass
            elif ppd == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()

            else:
                tagerechn1 = float(tage) + 1
                if lango == "DE":
                    listename = f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage liste.txt"
                elif lango == "ENG":
                    listename = f"from {str(start)} with {str(ppd)}% for {str(tage)} days list.txt"

                if liste == True:
                    if os.path.exists(listename):
                        if lango == "DE":
                            print("genau diese datei gibt es bereits")
                        elif lango == "ENG":
                            print("This file already exists.")
                        liste = False
                    else:
                        file = open(str(listename), "a", encoding='utf-8')
                        if lango == "DE":
                            file.write(f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage :\n")
                        elif lango == "ENG":
                            file.write(f"from {str(start)} with {str(ppd)}% for {str(tage)} days:\n")
                        file.close()
                else:
                    if lango == "DE":
                        print("du hast dich gegen die liste entschieden")

                    elif lango == "ENG":
                         print("You have decided against the list.")

                tagedone = 0
                startr = 0
                startold = start
                profitactuall = 0
                profitber = (float(ppd) / 100) + 1
                profitactuallr = 0

                while float(tagedone) < float(tagerechn1):
                    profitactuall = (float(start) - float(startold))
                    startold = start
                    profitactuallr = round(float(profitactuall), 2)
                    startr = round(float(startold), 2)
                    if liste == True:
                        if tagep == True:
                            file = open(str(listename), "a")
                            if lango == "DE":
                                file.write(f"tag{str(tagedone)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            elif lango == "ENG":
                                file.write(f"day{str(tagedone)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            file.close()
                        elif datump == True:
                            file = open(str(listename), "a")
                            todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                            today += datetime.timedelta(days=1)
                            file.write(f"{str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            file.close()
                        elif tageudatump == True:
                            file = open(str(listename), "a")
                            todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                            today += datetime.timedelta(days=1)
                            if lango == "DE":
                                file.write(f"tag {str(tagedone)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            elif lango == "ENG":
                                file.write(f"day {str(tagedone)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            file.close()
                    start = float(start) * float(profitber)
                    tagedone += 1
                if lango == "DE":
                    print(str(startr), "bei", str(ppd), "%")
                    neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                elif lango == "ENG":
                    print(str(startr), "at", str(ppd), "%")
                    neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()

                if neustart == "n":
                    pass
                else:
                    if lango == "DE":
                        input("zum schließen irgendeine taste drücken")
                    elif lango == "ENG":
                        input("Press any key to close")
                    exit()

        elif auswahl == "z":
            if lango == "DE":
                print("du bist im zeit such bereich")
                start = input("start angeben : ")
                ziel = input("Ziel eingeben : ")
                ppd = input("wass ist ein realistischer profit in % pro tag : ")
            elif lango == "ENG":
                print("You are in the time search area")
                start = input("Enter the start: ")
                ziel = input("Enter the target: ")
                ppd = input("What is a realistic profit in % per day: ")

            tagen = 0
            startr = 0

            if start == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif start == "n":
                if lango == "DE":
                    print("neustart")
                elif lango == "ENG":
                    print("restarting")
                pass
            elif ziel == "n":
                if lango == "DE":
                    print("neustart")
                elif lango == "ENG":
                    print("restarting")
                pass
            elif ziel == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif ppd == "n":
                if lango == "DE":
                    print("neustart")
                elif lango == "ENG":
                    print("restarting")
                pass
            elif ppd == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            else:
                if lango == "DE":
                    listename = f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} liste.txt"
                elif lango == "ENG":
                    listename = f"from {str(start)} with {str(ppd)} % to {str(ziel)} list.txt"

                if liste == True:
                    if os.path.exists(listename):
                        if lango == "DE":
                            print("genau diese datei gibt es bereits")
                        elif lango == "ENG":
                            print("This file already exists.")
                        liste = False
                    else:
                        file = open(str(listename), "a")
                        if lango == "DE":
                            file.write(f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} : \n")
                        elif lango == "ENG":
                            file.write(f"from {str(start)} with {str(ppd)}% to {str(ziel)}:\n")
                        file.close()
                else:
                    if lango == "DE":
                        print("du hast dich gegen die liste entschieden")
                    elif lango == "ENG":
                        print("You have decided against the list.")

                if start == "0":
                    if lango == "DE":
                        print("der startpunkt ist zu klein!")
                    elif lango == "ENG":
                        print("your start is to small")
                else:
                    rechn1 = (float(ppd) / 100) + 1
                    startold = start
                    profitactuall = 0
                    profitactuallr = 0

                    while float(start) < float(ziel):
                        profitactuall = (float(start) - float(startold))
                        startold = start
                        profitactuallr = round(float(profitactuall), 2)
                        startr = round(float(startold), 2)
                        start = float(start) * float(rechn1)
                        if liste == True:
                            file = open(str(listename), "a")
                            if tagep == True:
                                if lango == "DE":
                                    file.write(f"tag{str(tagen)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                elif lango == "ENG":
                                    file.write(f"day{str(tagen)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            elif datump == True:
                                todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                                today += datetime.timedelta(days=1)
                                file.write(f"{str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            elif tageudatump == True:
                                file = open(str(listename), "a")
                                todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                                today += datetime.timedelta(days=1)
                                if lango == "DE":
                                    file.write(
                                        f"tag {str(tagen)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                elif lango == "ENG":
                                    file.write(
                                        f"day {str(tagen)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                file.close()
                        tagen += 1
                    if float(start) > float(ziel):
                        profitactuallrest = (float(ziel) - float(startold))
                        profitactuallrestr = round(float(profitactuallrest), 2)
                        if liste == True:
                            file = open(str(listename), "a")
                            if tagep == True:
                                if lango == "DE":
                                    file.write(f"tag{str(tagen)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                elif lango == "ENG":
                                    file.write(f"day{str(tagen)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                file.close()
                            elif datump == True:
                                todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                                today += datetime.timedelta(days=1)
                                file.write(f"{str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            elif tageudatump == True:
                                file = open(str(listename), "a")
                                todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                                today += datetime.timedelta(days=1)
                                if lango == "DE":
                                    file.write(
                                        f"tag {str(tagen)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                elif lango == "ENG":
                                    file.write(
                                        f"day {str(tagen)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                file.close()

                    if lango == "DE":
                        print("es braucht ", str(tagen), "tag(e) bis du ", str(ziel), "erreicht hast")
                        neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                    elif lango == "ENG":
                        print("It takes ", str(tagen), " day(s) for you to reach ", str(ziel))
                        neustart = input("n for restart, any other key to exit: ").lower()

                    if neustart == "n":
                        pass
                    else:
                        if lango == "DE":
                            input("zum schließen irgendeine taste drücken")
                        elif lango == "ENG":
                            input("Press any key to close")
                        exit()

        elif auswahl == "t":
            if lango == "DE":
                print("du bist im tage bereich")
                start = input("startpunkt eingeben : ")
                ziel = input("gib dein ziel ein : ")
                tage = input("wie viele tage hast du zeit : ")
            elif lango == "ENG":
                print("You are in the days area")
                start = input("Enter the starting point: ")
                ziel = input("Enter your goal: ")
                tage = input("How many days do you have: ")

            if start == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif start == "n":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif tage == "n":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif tage == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif ziel == "n":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            elif ziel == "x":
                if lango == "DE":
                    print("abgebrochen")
                    input("sicher?")
                elif lango == "ENG":
                    print("Canceled")
                    input("Are you sure?")
                exit()
            else:
                if lango == "DE":
                    listename = f"von {str(start)} zu {str(ziel)} in {str(tage)} tagen liste.txt"
                elif lango == "ENG":
                    listename = f"from {str(start)} to {str(ziel)} in {str(tage)} days list.txt"

                tagerechn1 = float(tage) + 1
                mindtage = 1

                if float(tage) < float(mindtage):
                    if lango == "DE":
                        print("du hast zu wenig tage eingegeben bitte versuche es erneut")
                        tage = input("tage wiederholen : ")
                    elif lango == "ENG":
                        print("You have entered too few days. Please try again.")
                        tage = input("Repeat the number of days: ")
                    else:
                        print("")

                A = float(start)
                E = float(ziel)
                T = float(tage)
                # rechnung, do not touch !!!
                P = ((E / A) ** (1 / T)) - 1

                proz = float(P) * 100
                prozr = round(proz, 2)

                if liste == True:
                    if os.path.exists(listename):
                        if lango == "DE":
                            print("genau diese datei gibt es bereits")
                        elif lango == "ENG":
                            print("This file already exists.")
                        liste = False
                    else:
                        file = open(str(listename), "a", encoding='utf-8')
                        if lango == "DE":
                            file.write(f"von {str(start)} zu {str(ziel)} in {str(tage)} benötigt : {str(prozr)} % \n")
                            file.write(f"das Kapital würde so aussehen : \n")
                        elif lango == "ENG":
                            file.write(f"from {str(start)} to {str(ziel)} in {str(tage)} required: {str(prozr)}%\n")
                            file.write("The capital would look like this:\n")
                        file.close()

                    tagedone = 0
                    startr = 0
                    tagen = 0
                    startold = start
                    profitactuall = 0
                    profitactuallr = 0
                    profitber = (float(proz) / 100) + 1
                    while float(tagedone) < float(tagerechn1):
                        profitactuall = (float(start) - float(startold))
                        startold = start
                        profitactuallr = round(float(profitactuall), 2)
                        startr = round(float(startold), 2)
                        if liste == True:
                            file = open(str(listename), "a")
                            if tagep == True:
                                if lango == "DE":
                                    file.write(f"tag{str(tagen)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                elif lango == "ENG":
                                    file.write(f"day{str(tagen)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            elif datump == True:
                                todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                                today += datetime.timedelta(days=1)
                                file.write(f"{str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            elif tageudatump == True:
                                file = open(str(listename), "a")
                                todayuse = (f'{today.strftime("%d")}.{today.strftime("%m")}.{today.strftime("%Y")}')
                                today += datetime.timedelta(days=1)
                                if lango == "DE":
                                    file.write(
                                        f"tag {str(tagedone)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                                elif lango == "ENG":
                                    file.write(
                                        f"day {str(tagedone)} / {str(todayuse)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            file.close()
                        start = float(start) * float(profitber)
                        tagedone += 1
                if lango == "DE":
                    print("es braucht ca.", str(prozr), "% pro tag")
                elif lango == "ENG":
                    print("It takes about ", str(prozr), "% per day.")

                if lango == "DE":
                    neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                elif lango == "ENG":
                    neustart = input("n for restart, any other key to exit: ").lower()
                if neustart == "n":
                    pass
                else:
                    if lango == "DE":
                        input("zum schließen irgendeine taste drücken")
                    elif lango == "ENG":
                        input("Press any key to close")
                    exit()

        elif auswahl == "a":
            if lango == "DE":
                print("du bist im variablen bereich")
                addvarnam = input("gib den namen der variable ein : ").lower()
            elif lango == "ENG":
                print("You are in the variables area")
                addvarname = input("Enter the name of the variable: ").lower()

            if addvarnam[0].isalpha() and all(char.isalnum() or char in ['-', '_'] for char in addvarnam[1:]):
                if lango == "DE":
                    addvarz = input(f"gebe den wert der variable {addvarnam} ein : ")
                elif lango == "ENG":
                    addvarz = input(f"Enter the value of the variable {addvarnam}: ")
                if addvarz.isdigit():
                    if lango == "DE":
                        print(f"deine variable heißt jetzt {addvarnam} und ist {addvarz} wert")
                    elif lango == "ENG":
                        print(f"Your variable is now named {addvarnam} and is worth {addvarz}.")
                    file = open("safe_data.json", "r")
                    jsonlesen = file.read()
                    file.close()
                    jsonlesbar = jsonlesen.replace("\n", "")
                    newvar1 =jsonlesbar.replace("{", "")
                    newvar2 = newvar1.replace("}", "")
                    file = open(str(jsonfile), "w")
                    file.write("{")
                    file.write(f"\n{str(newvar2)},\"{str(addvarnam)}\": {str(addvarz)}\n")
                    file.write("}")
                    file.close()
                else:
                    if lango == "DE":
                        print("Ungültige Eingabe. Bitte geben Sie beim wert nur Zahlen ein.")
                    elif lango == "ENG":
                        print("Invalid input. Please enter only numbers for the value.")
            else:
                if lango == "DE":
                    print("Ungültige Eingabe. Bitte benutze keine zahlen an erster stelle und keine sonderzeichen außer - und _")
                elif lango == "ENG":
                    print("Invalid input. Please do not use numbers at the beginning and avoid specialcharacters except - and _.")

            if lango == "DE":
                neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
            elif lango == "ENG":
                neustart = input("n for restart, any other key to exit: ").lower()

            if neustart == "n":
                pass
            else:
                if lango == "DE":
                    input("zum schließen irgendeine taste drücken")
                elif lango == "ENG":
                    input("Press any key to close")
                exit()
        else:
            if lango == "DE":
                print("fehler bitte drücke nur z oder t oder b")
            elif lango == "ENG":
                print("Error, please only press z, t, or b.")
            if lango == "DE":
                neustart = input("drücke n zum erneuten versuchen : ").lower()
            elif lango == "ENG":
                neustart = input("Press n to try again: ").lower()

            if neustart == "n":
                pass
            else:
                if lango == "DE":
                    input("zum schließen irgendeine taste drücken")
                elif lango == "ENG":
                    input("Press any key to close")
                exit()

