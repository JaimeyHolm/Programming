stations = ("Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht")

def inlezen_beginstation(stations):
    beginStation = input('Wat is uw beginstation? ')
    while beginStation not in stations:
        print('Deze trein komt niet in ' + beginStation + '\n')
        beginStation = input('Begin? ')
    return beginStation

def inlezen_eindstation(stations, beginStation):
    eindStation = input('Wat is uw eindstation? ')
    while eindStation not in stations:
        print('Deze trein komt niet in ' + eindStation + '\n')
        eindStation = input('Wat is uw eindstation? ')

    while stations.index(eindStation) < stations.index(beginStation):
        print('Met deze trein komt u niet in ' + eindStation + '\n')
        eindStation = input('Wat is uw eindstation? ')

    return eindStation

def omroepen_reis(stations, beginStation, eindStation):
    print('Het beginstation', beginStation,  'is het', (stations.index(beginStation) + 1), 'e station in het traject.')
    print('Het eindstation', eindStation, 'is het', (stations.index(eindStation) + 1), 'e station in het traject.')
    print('De afstand bedraagt', (stations.index(eindStation) + 1) - (stations.index(beginStation) + 1), 'station(s).')
    print('De prijs van het kaartje is', (((stations.index(eindStation) + 1) - (stations.index(beginStation) + 1)) * 5), 'euro.')

stations = ("Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht")

beginStation = inlezen_beginstation(stations)
eindStation = inlezen_eindstation(stations, beginStation)

print(omroepen_reis(stations, beginStation, eindStation))