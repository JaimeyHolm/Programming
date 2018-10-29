def gemiddelde(zin):
    gesplit = zin.split(' ')
    lengteLijst = len(gesplit)
    i = 0
    aantal = []
    while i < lengteLijst:
        aantal.append(len(gesplit[i]))
        i += 1
    return sum(aantal) / lengteLijst

zin = input('Typ een zin: ')
print(gemiddelde(zin))

