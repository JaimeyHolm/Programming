invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

los = invoer.split('-')
gesorteerd = (los.sort())
grootst = max(los)
kleinst = min(los)
aantal = len(los)
tdlLijst = []

for getal in range(len(los)):
    tmp = int(los[getal])
    tdlLijst.append(tmp)
alles = sum(tdlLijst)

print('Gesorteerde list van ints: ' + str(los))
print('Grootste getal: ' + grootst + ' en Kleinste getal: ' + kleinst)
print('Aantallen getallen ' + str(aantal) + ' en Som van de getallen: ' + str(alles))
print('Gemiddelde: ' + str(alles / aantal))












