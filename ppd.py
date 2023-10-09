import os
liste = False
sauswahl = input("willst du deín ergebnis speichern ? JA/Nein :").lower()

if sauswahl == "ja":
    liste = True
else:
    liste = False
auswahl = input(
    "drücke z zum ziel berechnen oder b zum berechnen vom endergebnis oder t für eine anzahl an tagen : ").lower()

if auswahl == "b":

    print("du bist im berechnen bereich")

    start = input("start angeben : ")

    tage = input("tage eingeben : ")

    ppd = input("prozent pro tag eingeben : ")

    tagerechn1 = float(tage) + 1

    listename = f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage liste.txt"

    if liste == True:
        if os.path.exists(listename):
            print("genau diese datei gibt es bereits")
            liste = False
        else:
            file = open(str(listename), "a")
            file.write(f"von {str(start)} mit {str(ppd)} % für {str(tage)} tage : \n")
            file.close()
    else:
        print("du hast dich gegen die liste entschieden")

    tagedone = 0
    startr = 0

    profitber = (float(ppd) / 100) + 1
    while float(tagedone) < float(tagerechn1):
        startr = round(float(start), 2)
        if liste == True:
            file = open(str(listename), "a")
            file.write(f"tag {str(tagedone)} : {str(startr)} \n")
            file.close()
        start = float(start) * float(profitber)
        tagedone += 1

    print(str(startr), "bei", str(ppd), "%")
    input("zum schließen irgendeine taste drücken")


elif auswahl == "z":
    print("du bist im zeit such bereich")
    start = input("start angeben : ")
    ziel = input("Ziel eingeben : ")
    ppd = input("wass ist ein realistischer profit in % pro tag : ")
    tagen = 1
    startr = 0
    listename = f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} liste.txt"

    if liste == True:
        if os.path.exists(listename):
            print("genau diese datei gibt es bereits")
            liste = False
        else:
            file = open(str(listename), "a")
            file.write(f"von {str(start)} mit {str(ppd)} % bis {str(ziel)} : \n")
            file.write(f"tag : 0 : geld : {str(start)} \n")
            file.close()
    else:
        print("du hast dich gegen die liste entschieden")

    if start == "0":
        print("der startpunkt ist zu klein!")
    else:
        rechn1 = (float(ppd) / 100) + 1

        while float(start) < float(ziel):
            startr = round(float(start), 2)
            start = float(start) * float(rechn1)
            if liste == True:
                file = open(str(listename), "a")
                file.write(f"tag : {str(tagen)} : geld : {str(startr)} \n")
                file.close()
            tagen += 1
        if float(start) > float(ziel):
            print(end="")

            if liste == True:
                file = open(str(listename), "a")
                file.write(f"tag : {str(tagen)} : geld : {str(ziel)} \n")
                file.close()

        print("es braucht ", str(tagen), "tag(e) bis du ", str(ziel), "erreicht hast")
        input("zum schließen irgendeine taste drücken")

        # print(float(start), float(ziel), float(ppd))
elif auswahl == "t":
    print("du bist im tage bereich")
    start = input("startpunkt eingeben : ")
    ziel = input("gib dein ziel ein : ")
    tage = input("wie viele tage hast du zeit : ")
    listename = f"von {str(start)} zu {str(ziel)} in {str(tage)} tagen liste.txt"
    tagerechn1 = float(tage) + 1
    mindtage = 1

    if float(tage) < float(mindtage) :
        print("du hast zu wenig tage eingegeben bitte versuche es erneut")
        tage = input("tage wiederholen : ")
    else:
        print(end="")

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
            file = open(str(listename), "a")
            file.write(f"von {str(start)} zu {str(ziel)} in {str(tage)} benötigt : {str(prozr)} % \n")
            file.write(f"das Kapital würde so aussehen : \n")
            file.close()

        tagedone = 0
        startr = 0

        profitber = (float(proz) / 100) + 1
        while float(tagedone) < float(tagerechn1):
            startr = round(float(start), 2)
            if liste == True:
                file = open(str(listename), "a")
                file.write(f"tag {str(tagedone)} : {str(startr)} \n")
                file.close()
            start = float(start) * float(profitber)
            tagedone += 1

    print("es braucht ca.", str(prozr), "% pro tag")
    input("zum schließen irgendeine taste drücken")
else:
    print("fehler bitte drücke nur z oder t oder b")
    input("zum schließen irgendeine taste drücken")
