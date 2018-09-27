def seizoen(maand):
    if maand == 12 or maand == 1 or maand == 2:
        return('Winter')
    elif maand == 3 or maand == 4 or maand == 5:
        return('Lente')
    elif maand == 6 or maand == 7 or maand == 8:
        return('Zomer')
    elif maand == 9 or maand == 10 or maand == 11:
        return('Herfst')


maand = int(input('Hoeveelste maand is het? '))

print(seizoen(maand))