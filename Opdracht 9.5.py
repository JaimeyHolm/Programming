def namen():
    namen = []
    while True:
        naam = input('Volgende naam: ')
        if naam != '':
            namen.append(naam)
            aantal = {}
            for naam in namen:
                if naam in aantal:
                    aantal[naam] += 1
                else:
                    aantal[naam] = 1
        else:
            break
    return aantal

print(namen())

