from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    korting_prijs = prijs - korting * prijs
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting_prijs} euro."

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    return totaal

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    bedrag = btw * totaal
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst), max(mijn_lijst)

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    laag_en_hoog = min(invoer_lijst), max(invoer_lijst)
    return laag_en_hoog

print(meervoudig([10,5,3,2,1,2,9]))
