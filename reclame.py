from algemene_functies import mijn_functie2 

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro"

# Test de aanbieding_1 functie met de opgegeven argumenten
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    totaal_inkomsten = sum(inkomsten)
    return totaal_inkomsten
def inkomsten_totaal(inkomsten, btw=0):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

# Test de inkomsten_totaal functie met een voorbeeldlijst van inkomsten per dag
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
def inkomsten_totaal(inkomsten, btw=0.21):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

print(inkomsten_totaal(inkomsten_per_dag, btw_percentage))
def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [hoogste, laagste]

# Test de laag_en_hoog functie met een voorbeeldlijst van inkomsten per dag
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten_per_dag)
print(f"De hoogste inkomst van deze week is {resultaat[0]} euro en de laagste inkomst is {resultaat[1]} euro.")

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal_dagen = len(mijn_lijst)
    gemiddelde_inkomsten = totaal / aantal_dagen
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."

# Test de gemiddelde functie met een voorbeeldlijst van inkomsten per dag
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
gemiddelde_inkomsten_per_dag = gemiddelde(inkomsten_per_dag)
print(gemiddelde_inkomsten_per_dag)
def combinatie(invoer_lijst_2):
    print("Invoerlijst 2:", invoer_lijst_2)
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    print("Korte lijst na laag_en_hoog:", korte_lijst)
    resultaat_mijn_functie2 = mijn_functie2(korte_lijst)
    print("Resultaat mijn_functie2:", resultaat_mijn_functie2)
    return resultaat_mijn_functie2