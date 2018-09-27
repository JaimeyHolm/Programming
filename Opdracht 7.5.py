zin = input('Typ een zin: ')

def gemiddelde(zin):
    gesplit = zin.split(' ')
    lengteLijst = len(gesplit)
    i = 0
    aantal = []
    while i < lengteLijst:
        aantal.append(len(gesplit[i]))
        i += 1
    return len(aantal) / lengteLijst


print(gemiddelde(zin))

