import csv

from helper import som
from presentatie import presenteer

inkomsten = {'Aardbeien-ijs-totaal': 1000, 'Vanille-ijs-totaal': 2000, 'Chocolade-ijs-totaal': 1500, 'Waterijsjes-totaal': 750}

totaal_inkomsten = som(inkomsten)

print("De totale inkomsten zijn:", totaal_inkomsten)

def inkomsten():
    uitvoer = []
    uitvoer.append("Aardbeien-ijs-totaal: 1000")
    uitvoer.append("Vanille-ijs-totaal: 2000")
    uitvoer.append("Chocolade-ijs-totaal: 1500")
    uitvoer.append("Waterijsjes-totaal: 750")
    
    return uitvoer

resultaten = inkomsten()

for el in resultaten:
    print(el)

inkomsten = { 
'Aardbeien-ijs': 1000,
 'Vanille-ijs': 2000,
 'Chocolade-ijs': 1500,
 'Waterijsjes': 750
} 

totaal_inkomsten = sum(inkomsten.values())

presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
      writer = csv.writer(csvfile, delimter=';')
      writer.writerow([key,value])