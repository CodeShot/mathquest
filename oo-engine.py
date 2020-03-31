# Syftet med att göra detta objektorienterat är att illustrera hur man på så sätt kan särskilja olika
# delar ifrån varandra. I den här modulen kommer endast banor och allt som har med dessa att göra förekomma.
# för att sedan ha ett gränssnitt så måste det definieras i en separat modul som nyttjar/importerar denna
# moduls funktionalietet


from random import randint, uniform
from datetime import datetime


r"""
    bana - är basklass som sedan kommer ärvas av varje enkild typ av bana

    detta sätt göra kallas polymorfism och innebär att man har en basklass som har de gemensamma egenskaperna
    definierade, detta kan vara variabler som namn, egenskaper och metoder som skapa_uppgifter(), rätta_uppgifter() osv..
"""
class bana(object):
    # objektet spelare och uppgifter förvänstas se ut som nedan angivet
    #
    # spelare = { "<spelarnamn>": [UUID, ...] }
    # uppgifter = { "<datum och tid>" : ["bana", "nivå", "<påbörjad>", "<tid>", ["<uttryck>", facit, svar, utfall]], ... }
    #


    # nivåindelat talset som går att byta ut i en specifik instans
    # format: talset = { "<nivånummer">: (<start>, <stop>, <antal decimaler>), ... }
    talset = { 1: (1, 9, 0),
               2: (1, 100, 0),
               3: (1, 1000, 0),
               4: (0.1, 10.0, 1),
               5: (0.01, 100.00, 2) }

    uppgifter = dict()

    def __init__(self, *args):
        raise NotImplementedError(r"Denna metod måste implementeras!")

    def skapa_uppgifter(self, nivå, antal):
        raise NotImplementedError(r"Denna metod måste implementeras!")


class banaAddition(bana):
    def __init__(self, spelare):
        self.namn = "Addition"
        self.spelare = spelare


    def skapa_uppgifter(self, nivå, antal):
        if nivå < 4:
            talpar = hjälpare.skapa_talparserie(self.talset[nivå], antal)
        else:
            talpar = hjälpare.skapa_flyttalparserie(self.talset[nivå], antal)

        uppg = [self.namn, str(nivå), "", "", []] # så element 4 innehåller lista med uppgifter

        print("%s", talpar)

        for par in talpar:
            uttryck = "%s + %s" % par
            uppg[4].append([uttryck, eval(uttryck), None, None])

        self.uppgifter[datetime.now()] = uppg

class banaSubtraktion(bana):
    def __init__(self, spelare):
        self.namn = "Subtraktion"
        self.spelare = spelare


    def skapa_uppgifter(self, nivå, antal):
        if nivå < 4:
            talpar = hjälpare.skapa_talparserie(self.talset[nivå], antal)
        else:
            talpar = hjälpare.skapa_flyttalparserie(self.talset[nivå], antal)

        uppg = [self.namn, str(nivå), "", "", []] # så element 4 innehåller lista med uppgifter

        for par in talpar:
            if (nivå < 4) and (par[0] < par[1]):
                par = (par[1], par[0])

            uttryck = "%s - %s" % par
            uppg[4].append([uttryck, eval(uttryck), None, None])

        self.uppgifter[datetime.now()] = uppg


class banaMultiplikation(bana):
    def __init__(self, spelare):
        self.namn = "Multiplikation"
        self.spelare = spelare


    def skapa_uppgifter(self, nivå, antal):
        if nivå < 4:
            talpar = hjälpare.skapa_talparserie(self.talset[nivå], antal)
        else:
            talpar = hjälpare.skapa_flyttalparserie(self.talset[nivå], antal)

        uppg = [self.namn, str(nivå), "", "", []] # så element 4 innehåller lista med uppgifter

        for par in talpar:
            uttryck = "%s * %s" % par
            uppg[4].append([uttryck, round(eval(uttryck), self.talset[nivå][2]), None, None])

        self.uppgifter[datetime.now()] = uppg



class banaDivision(bana):
    def __init__(self, spelare):
        self.namn = "Division"
        self.spelare = spelare


    def skapa_uppgifter(self, nivå, antal):
        if nivå < 4:
            talpar = hjälpare.skapa_talparserie(self.talset[nivå], antal)
        else:
            talpar = hjälpare.skapa_flyttalparserie(self.talset[nivå], antal)

        uppg = [self.namn, str(nivå), "", "", []] # så element 4 innehåller lista med uppgifter

        for par in talpar:
            if par[0] < par[1]:
                par = (par[1], par[0])

            uttryck = "%s / %s" % par
            uppg[4].append([uttryck, round(eval(uttryck), self.talset[nivå][2]), None, None])

        self.uppgifter[datetime.now()] = uppg



r"""
    dessa funktioner är hjälpfunktioner för att kunna skapa tal och uttryck
    därför kallar vi dem för hjälpare.
    metoderna är statiska vilket innebär att de inte kan påverkar själva hjälpar-objektet,
    således behöver inte ett hjälpar-objekt instantieras innan man kör statiska metoder.
    så effekten är mest kosmetisk då dessa metoder blir "samlade" eller kategoriserade.
"""

class hjälpare(object):
    @staticmethod
    def skapa_talparserie(talset, antal):
        resultat = []

        for n in range(antal):
            taltup = (randint(talset[0], talset[1]), randint(talset[0], talset[1]))

            resultat.append(taltup)

        return(resultat)

    @staticmethod
    def skapa_flyttalparserie(talset, antal):
        resultat = []

        for n in range(antal):
            taltup = (round(uniform(talset[0], talset[1]), talset[2]), round(uniform(talset[0], talset[1]), talset[2]))

            resultat.append(taltup)

        return(resultat)



if __name__ == "__main__":
    addition = banaAddition("spelare 1")
    subtraktion = banaSubtraktion("spelare 2")
    multiplikation = banaMultiplikation("spelare 3")
    division = banaDivision("spelare 4")

    addition.skapa_uppgifter(1, 20)
    print(addition.uppgifter)
