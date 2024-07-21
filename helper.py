def decoreer(tekst=""):
        tekst="header"
        lengte = len(tekst) + 4
        print() 
        print(lengte * "*")
        print(f"* {tekst} *")
        print(lengte * "*")
        print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen 
    return f"Het bedrag per persoon is {bedrag_pp} euro"       
def onderstreep(tekst=""):
                uit = []
                uit.append(tekst)
                uit.append(len(tekst) * "=")
                return uit
from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")    
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")
print()

for el in uitvoer:
        print(el)

def som(dictionary):
    return sum(dictionary.values())
