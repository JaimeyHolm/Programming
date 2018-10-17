import datetime
import csv

def omzettenASCII(omzetWaarde):
    lijst = list(omzetWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) - 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin


def terugomzettenASCII(omgezetteWaarde):
    lijst = list(omgezetteWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) + 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin


def infoPubliek():
    with open('stalling.csv', 'r', newline='') as myCSVFile:
        lezer = csv.DictReader(myCSVFile, delimiter=',')
        aantalRegels = 0
        stallingBezet = []
        for regel in lezer:
            aantalRegels += 1
            omgezet = terugomzettenASCII(regel['pq^iifkd'])
            stallingBezet.append(omgezet)
        return stallingBezet

def plekVrij():
    invoer = input('Welk kluisnummer wilt u? ')
    if invoer in infoPubliek():
        print('Deze stallingsplaats is al in gebruik.')
    else:
        wachtwoordStallingsplaats = input('Voer een wachtwoord in voor uw stallingsplaats: ')
        while ',' in wachtwoordStallingsplaats:
            print('Uw wachtwoord mag geen komma bevatten.')
            wachtwoordStallingsplaats = input('Voer een wachtwoord in voor uw stallingsplaats: ')

        else:
            wachtwoord = omzettenASCII(wachtwoordStallingsplaats)
            vandaag = datetime.datetime.today()
            s = vandaag.strftime("%d-%b-%Y, %I:%M:%S")
            datum = omzettenASCII(s)
            return wachtwoord, datum


print('Deze kluizen zijn in gebruik:', infoPubliek())
print('Kies een kluis van 1 t/m 99 die niet bezet is.')

print(plekVrij())