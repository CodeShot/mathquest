import os
from random import randrange, uniform
import math
import sys


spelare = dict()
spelare["Alla Resulat"] = []
spelare["Nytt Resultat"] = False
spelare["Senaste Resultat"] = []

def starta_spel():
    utfall = True

    while(utfall):
        utfall = huvudmeny()

        if(utfall == 0):
            break

    avsluta_spel()


def avsluta_spel(x):
    sys.exit(0)


# <<< TEXTGRÄNSSNITT

def huvudmeny():
    os.system("clear")

    print("(1) Addition")

    print("(2) Subtraktion")

    print("(3) Multiplikation")

    print("(4) Division")

    print("(5) Ekvationer I")

    print("(6) Bråk och Procent")

    print("(7) Ekvationer II")

    print("(x) Om spelet")

    print("(s) Stäng av")

    if(spelare["Nytt Resultat"]):
        skriv_ut_resultat(spelare["Senaste Resultat"])

        spelare["Nytt Resultat"] = False

    svar = input("Alternativ: ")

    if svar in banor.keys():
        banor[svar](1)

    return(2)


def om_spelet(x):
    os.system("clear")
    print("Alla banor har svårighetsgrader")
    print("För att öppna upp nya banor måste man först ha klarat minst 5 svårighetsgrader på addition och subtraktion")
    print("För att fortsätta öppna upp banor måste man klara tre ytterligare svårighetsgrader för varje ny värld")

    ans = input("Tryck <ENTER>")

    return(2)


## << ADDITION OCH SUBTRAKTION BANOR OCH TUI
def _fråga_om_nivå(räknesätt, nivåer):
    while(True):
        print("Välj nivå på banan")
        print("   -- ----- --")
        print("(1) %s med tal 1 - 9" % räknesätt)
        print("(2) %s med tal 1 - 100" % räknesätt)
        print("(3) %s med tal 1 - 1000" % räknesätt)
        print("(4) %s med 0.0  - 10.0" % räknesätt)
        print("(5) %s med 0.00 - 100.00" % räknesätt)
        print("(x) Tillbaka till huvudmenyn")

        val = input("Välj nivå: ")

        if(val == "x"):
            return(2)
        elif(val in nivåer.keys()):
            return(val)


def skriv_ut_resultat(resultat):
    for r in resultat:
        # lista med utseende [[uppgift, facit, angivet, sanningsvärde], ...]
        print("%s = %s, svar: %s  -- %s" % (r[0], r[1], r[2], "Rätt" if r[3] else "Fel"))


def visa_uppgifter(uppgifter):
    löst = []

    for uppgift in uppgifter["uppgifter"]:
        svar = input("%s = " % uppgift[0])
        print("")
        löst.append([uppgift[0], uppgift[1], str(svar)])

    uppgifter["uppgifter"] = löst


def bana_addition(nivå):
    talset = { "1": (1, 9, 0),
               "2": (1, 100, 0),
               "3": (1, 1000, 0),
               "4": (0.0, 10.0, 1),
               "5": (0.00, 100.00, 2) }


    val = _fråga_om_nivå("Addition", talset)

    if(val in talset.keys()):
        if(int(val) > 3):
            taltup = generera_flyttaltupler(talset[val], 2, 5)
        else:
            taltup = generera_taltupler(talset[val], 2, 5)

    if(val == 2):
        return(2)

    uppgifter = skapa_uppgifter("+", taltup, talset[val])

    visa_uppgifter(uppgifter)

    rätta_uppgifter(uppgifter)

    return(2)


def bana_subtraktion(nivå):
    talset = { "1": (1, 9, 0),
               "2": (1, 100, 0),
               "3": (1, 1000, 0),
               "4": (0.0, 10.0, 1),
               "5": (0.00, 100.00, 2) }


    val = _fråga_om_nivå("Subtraktion", talset)

    if(val in talset.keys()):
        if(int(val) > 3):
            taltup = generera_flyttaltupler(talset[val], 2, 5)
        else:
            taltup = generera_taltupler(talset[val], 2, 5, subtraktion = True)

    if(val == 2):
        return(2)

    uppgifter = skapa_uppgifter("-", taltup, talset[val])

    visa_uppgifter(uppgifter)

    rätta_uppgifter(uppgifter)

    return(2)


def bana_multiplikation(nivå):
    talset = { "1": (1, 9, 0),
               "2": (1, 100, 0),
               "3": (1, 1000, 0),
               "4": (0.0, 10.0, 1),
               "5": (0.00, 100.00, 2) }


    val = _fråga_om_nivå("Multiplikation", talset)

    if(val in talset.keys()):
        if(int(val) > 3):
            taltup = generera_flyttaltupler(talset[val], 2, 5)
        else:
            taltup = generera_taltupler(talset[val], 2, 5)

    if(val == 2):
        return(2)

    print("")
    print("Alla tal avrundas till %d decimaler" % talset[val][2])
    print("")


    uppgifter = skapa_uppgifter("*", taltup, talset[val])

    visa_uppgifter(uppgifter)

    rätta_uppgifter(uppgifter)

    return(2)


def bana_division(nivå):
    talset = { "1": (1, 9, 0),
               "2": (1, 100, 0),
               "3": (1, 1000, 0),
               "4": (0.0, 10.0, 1),
               "5": (0.00, 100.00, 2) }


    val = _fråga_om_nivå("Multiplikation", talset)

    if(val in talset.keys()):
        if(int(val) > 3):
            taltup = generera_flyttaltupler(talset[val], 2, 5)
        else:
            taltup = generera_taltupler(talset[val], 2, 5)

    if(val == 2):
        return(2)

    print("")
    print("Alla tal avrundas till %d decimaler" % talset[val][2])
    print("")


    uppgifter = skapa_uppgifter("*", taltup, talset[val])

    visa_uppgifter(uppgifter)

    rätta_uppgifter(uppgifter)

    return(2)


def bana_ekvationer(nivå):
    return(2)


def bana_algoritmer(nivå):
    return(2)


def bana_procent(nivå):
    return(2)


# <<< VARIABLER

banor = {
    "1": bana_addition,
    "2": bana_subtraktion,
    "3": bana_multiplikation,
    "4": bana_division,
    "5": bana_ekvationer,
    "6": bana_algoritmer,
    "7": bana_procent,
    "x": om_spelet,
    "s": avsluta_spel }

# <<< FUNKTIONALITET


def generera_taltupler(talset, dimension, antal, subtraktion=False):
    resultat = []

    for i in range(antal):
        taltup = [randrange(talset[0], talset[1], 1) for i in range(dimension)]
        if subtraktion and (taltup[0] < taltup[1]):
            t = taltup[0]
            taltup[0] = taltup[1]
            taltup[1] = t
 
        resultat.append(taltup)

    return(resultat)

def generera_flyttaltupler(talset, dimension, antal):
    resultat = []

    for i in range(antal):
        taltup = [round(uniform(talset[0], talset[1]), int(talset[2])) for i in range(dimension)]
        resultat.append(taltup)

    return(resultat)



def skapa_uppgifter(operand, taltupler, talset):
    uppgifter = dict()
    uppgifter["uppgifter"] = []

    for taltupel in taltupler:
        uttryck = str(taltupel[0])

        for t in taltupel[1:]:
            uttryck += " %s %s" % (operand, str(t))

            if(talset[2] > 0):
                svar = round(eval(uttryck), talset[2])
            else:
                svar = eval(uttryck)

            uppgifter["uppgifter"].append([uttryck, str(svar)])

    return(uppgifter)


def rätta_uppgifter(uppgifter):
    rättad = []
    for u in uppgifter["uppgifter"]:
        u.append(True if u[1] == u[2] else False)
        rättad.append(u)

    uppgifter["uppgifter"] = rättad
    spelare["Nytt Resultat"] = True
    spelare["Senaste Resultat"] = rättad





if __name__ == "__main__":
    starta_spel()
