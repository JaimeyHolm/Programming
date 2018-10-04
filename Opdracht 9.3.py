cijfers = {'Zwanetta': 6.0, 'Iona': 7.8, 'Ilse': 9.8, 'Clarinetta': 5.6, 'Kroketta': 9.7, 'Herman': 10.0}

for getal in cijfers:
    cijfer = cijfers[getal]
    if cijfer > 9.0:
        print (getal, end=': ')
        print(cijfer)