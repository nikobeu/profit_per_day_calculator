import os
import sys
import json

script_path = os.path.abspath(sys.argv[0])

parent_directory = (os.path.dirname(script_path))

nstart = (rf"start {str(parent_directory)}\start_ppd.cmd")

jsonfile = (rf"{str(parent_directory)}\safe_data.json")


if not os.path.exists(rf"{str(parent_directory)}\start_ppd.cmd"):
    file = open("start_ppd.cmd", "a")
    file.write(f"@echo off\n\n")
    file.write(rf"python {str(script_path)}")
    file.close()
    os.system(nstart)
    exit()
else:
    if not os.path.exists(rf"{str(parent_directory)}\safe_data.json"):
        file = open("safe_data.json", "a")
        file.write("{\n")
        file.write(f"\"var_1\": 0\n")
        file.write("}")
        file.close()

    idiotentest = True
    file = open("start_ppd.cmd", "r")
    idiotl1 = file.readline()
    idiotl2 = file.readline()
    idiotl3 = file.readline()
    file.close()
    if not idiotl1 == "@echo off\n":
        idiotentest = False
    elif not idiotl2 == "\n":
        idiotentest = False
    elif not idiotl3 == (rf"python {str(script_path)}"):
        idiotentest = False

    if idiotentest == False:
        file = open("start_ppd.cmd", "w")
        file.write(f"@echo off\n\n")
        file.write(rf"python {str(script_path)}")
        file.close()
        os.system(nstart)
        exit()
    else:
        file = open("safe_data.json", "r")
        jsonlesen = file.read()
        file.close()
        jsonlesbar = jsonlesen.replace("\n", "")
        jsoncmd = json.loads(jsonlesbar)
        availablejson = (f"s")

        #print(str(availablejson))
        liste = False
        print("wenn du stoppen willst drücke zu dem zeitpunkt x und wenn du irgendwann neustarten willst drücke n")
        sauswahl = input("willst du deín ergebnis speichern ? JA/Nein :").lower()
        if sauswahl == "x":
            print("abgebrochen")
            input("zum schließen irgendeine taste drücken")
            exit()
        elif sauswahl == "n":
            print("neustart")
            os.system(nstart)
            exit()
        elif sauswahl == "ja":
            liste = True
        else:
            liste = False
        auswahl = input(
            "drücke z zum ziel berechnen oder b zum berechnen vom endergebnis oder t für eine anzahl an tagen oder a für variablen : ").lower()

        if auswahl == "x":
            print("abgebrochen")
            input("zum schließen irgendeine taste drücken")
            exit()
        elif auswahl == "n":
            print("neustart")
            os.system(nstart)
            exit()
        elif auswahl == "b":

            print("du bist im berechnen bereich")

            start = input("start angeben : ")

            tage = input("tage eingeben : ")

            ppd = input("prozent pro tag eingeben : ")

            if start == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif start == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif ppd == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ppd == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()

            else:
                tagerechn1 = float(tage) + 1

                listename = f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage liste.txt"

                if liste == True:
                    if os.path.exists(listename):
                        print("genau diese datei gibt es bereits")
                        liste = False
                    else:
                        file = open(str(listename), "a", encoding='utf-8')
                        file.write(f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage : \n")
                        file.close()
                else:
                    print("du hast dich gegen die liste entschieden")

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
                        file = open(str(listename), "a")
                        file.write(f"tag {str(tagedone)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                        file.close()
                    start = float(start) * float(profitber)
                    tagedone += 1

                print(str(startr), "bei", str(ppd), "%")

                neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                if neustart == "n":
                    os.system(nstart)
                    exit()
                else:
                    input("zum schließen irgendeine taste drücken")
                    exit()

        elif auswahl == "z":
            print("du bist im zeit such bereich")
            start = input("start angeben : ")
            ziel = input("Ziel eingeben : ")
            ppd = input("wass ist ein realistischer profit in % pro tag : ")
            tagen = 0
            startr = 0

            if start == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif start == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ziel == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ziel == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif ppd == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ppd == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            else:
                listename = f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} liste.txt"

                if liste == True:
                    if os.path.exists(listename):
                        print("genau diese datei gibt es bereits")
                        liste = False
                    else:
                        file = open(str(listename), "a")
                        file.write(f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} : \n")
                        file.close()
                else:
                    print("du hast dich gegen die liste entschieden")

                if start == "0":
                    print("der startpunkt ist zu klein!")
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
                            file.write(f"tag : {str(tagen)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            file.close()
                        tagen += 1
                    if float(start) > float(ziel):
                        profitactuallrest = (float(ziel) - float(startold))
                        profitactuallrestr = round(float(profitactuallrest), 2)
                        if liste == True:
                            file = open(str(listename), "a")
                            file.write(f"tag : {str(tagen)} : {str(ziel)}  (+{float(profitactuallrestr)}$) \n")
                            file.close()

                    print("es braucht ", str(tagen), "tag(e) bis du ", str(ziel), "erreicht hast")

                    neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                    if neustart == "n":
                        os.system(nstart)
                        exit()
                    else:
                        input("zum schließen irgendeine taste drücken")
                        exit()

        elif auswahl == "t":
            print("du bist im tage bereich")
            start = input("startpunkt eingeben : ")
            ziel = input("gib dein ziel ein : ")
            tage = input("wie viele tage hast du zeit : ")

            if start == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif start == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif tage == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            elif ziel == "n":
                print("neustart")
                os.system(nstart)
                exit()
            elif ziel == "x":
                print("abgebrochen")
                input("zum schließen irgendeine taste drücken")
                exit()
            else:

                listename = f"von {str(start)} zu {str(ziel)} in {str(tage)} tagen liste.txt"
                tagerechn1 = float(tage) + 1
                mindtage = 1

                if float(tage) < float(mindtage):
                    print("du hast zu wenig tage eingegeben bitte versuche es erneut")
                    tage = input("tage wiederholen : ")
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
                        print("genau diese datei gibt es bereits")
                        liste = False
                    else:
                        file = open(str(listename), "a", encoding='utf-8')
                        file.write(f"von {str(start)} zu {str(ziel)} in {str(tage)} benötigt : {str(prozr)} % \n")
                        file.write(f"das Kapital würde so aussehen : \n")
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
                            file.write(f"tag {str(tagedone)} : {str(startr)}  (+{float(profitactuallr)}$) \n")
                            file.close()
                        start = float(start) * float(profitber)
                        tagedone += 1

                print("es braucht ca.", str(prozr), "% pro tag")

                neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
                if neustart == "n":
                    os.system(nstart)
                    exit()
                else:
                    input("zum schließen irgendeine taste drücken")
                    exit()
        elif auswahl == "a":
            print("du bist im variablen bereich")
            addvarnam = input("gib den namen der variable ein : ").lower()
            if addvarnam[0].isalpha() and all(char.isalnum() or char in ['-', '_'] for char in addvarnam[1:]):
                addvarz = input(f"gebe den wert der variable {addvarnam} ein : ")
                if addvarz.isdigit():
                    print(f"deine variable heißt jetzt {addvarnam} und ist {addvarz} wert")
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
                    print("Ungültige Eingabe. Bitte geben Sie beim wert nur Zahlen ein.")
            else:
                print("Ungültige Eingabe. Bitte benutze keine zahlen an erster stelle und keine sonderzeichen außer - und _")

            neustart = input("n für neustart, irgendeine andere taste zum verlassen : ").lower()
            if neustart == "n":
                os.system(nstart)
                exit()
            else:
                input("zum schließen irgendeine taste drücken")
                exit()
        else:
            print("fehler bitte drücke nur z oder t oder b")
            neustart = input("drücke n zum erneuten versuchen : ").lower()
            if neustart == "n":
                os.system(nstart)
                exit()
            else:
                input("zum schließen irgendeine taste drücken")
                exit()

input("durchgerutscht bitte debuggen")
