def kwadraten_som(grondgetallen):
    outputLijst = []
    for getal in grondgetallen:
        if getal > 0:
            getal = getal**2
            outputLijst.append(getal)
    return sum(outputLijst)


print(kwadraten_som([4, 5, 3, -81]))


