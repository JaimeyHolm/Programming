import csv

def lezen(informatie1, informatie2):
    with open('Opdracht 11.4.csv', 'r') as myCSVFile:
        reader = csv.DictReader(myCSVFile, delimiter=';')
        informatie1Lijst = []
        informatie2Lijst = []
        for regel in reader:
            temp = regel[informatie1]
            temp = float(temp)
            informatie1Lijst.append(temp)
            informatie2Lijst.append(regel[informatie2])
    return informatie1Lijst, informatie2Lijst

prijs, naam = lezen('Prijs', 'Naam')
voorraad, artikelnummer = lezen('Voorraad', 'Artikelnummer')
hoogstePrijs = max(prijs)
kleinsteVoorraad = min(voorraad)
kleinsteVoorraad = int(kleinsteVoorraad)
alles = sum(voorraad)
alles = int(alles)
naamHoogstePrijs = naam[prijs.index(hoogstePrijs)]
artikelcodeKleinsteVoorraad = artikelnummer[voorraad.index(kleinsteVoorraad)]
print('Het duurste artikel is {} en dat kost {} euro.'.format(naamHoogstePrijs, hoogstePrijs))
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}.'.format(kleinsteVoorraad, artikelcodeKleinsteVoorraad))
print('In totaal hebben wij {} producten in ons magazijn liggen.'.format(alles))