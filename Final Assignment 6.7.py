afstandKM = int(input('Hoeveel KM: '))
leeftijd = int(input('Geef je leeftijd: '))
weekendrit = (input('Geef de dag op: '))


while weekendrit != 'maandag' or weekendrit != 'dinsdag' or weekendrit != 'woensdag' or weekendrit != 'donderdag' or weekendrit != 'vrijdag' or weekendrit != 'zaterdag' or weekendrit != 'zondag':
    print('\n')
    print('De waarde die u heeft ingevuld voor "Geef de dag op" voldoet niet.')
    print('Graag bij het invullen de waarde "maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag" of "zondag" invullen.')
    weekendrit = (input('Geef de dag op: '))

def standaardprijs(afstandKM):
    if afstandKM <= 50 and afstandKM != 0:
        return (afstandKM * 0.80)

    elif afstandKM > 50:
        return (afstandKM * 0.60 + 15)

    elif afstandKM == 0:
        print ('€0.00')



def ritprijs(leeftijd, weekendrit, standaardprijs):
    rekenprijs = standaardprijs(afstandKM)
    if weekendrit == 'zaterdag' or weekendrit == 'zondag':
        if leeftijd < 12 or leeftijd >= 65:
            return round(rekenprijs*0.65, 2)
        else:
            return round(rekenprijs*0.60, 2)
    if weekendrit == 'maandag' or weekendrit == 'dinsdag' or weekendrit == 'woensdag' or weekendrit == 'donderdag' or weekendrit == 'vrijdag':
        if leeftijd < 12 or leeftijd >= 65:
            return round(rekenprijs*0.70, 2)
        else:
            return round(rekenprijs, 2)
    else:
        print(weekendrit + ' is geen geldige waarde van de dag.')

print (ritprijs(leeftijd, weekendrit, standaardprijs))

