#Deze code gebruiken om final assignment 10.5 te kunnen maken.
#Deze code is om te kijken hoeveelste station het ingevoerde station is.
#In plaats van "Heerhugowaard" op regel 5, de invoer van de gebruiker gebruiken.
stations = ("Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht")
print(stations.index("Heerhugowaard") + 1)

for station in range(int(stations.index('Schagen')+1), (int(stations.index('Alkmaar')))):
    print('- '+(stations[station]))