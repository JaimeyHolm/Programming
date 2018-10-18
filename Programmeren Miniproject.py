import datetime
import csv
import random

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
    with open('registreren.csv', 'r', newline='') as myCSVFile:
        while True:
            registratienummer = input('Wat is uw registratienummer? ')
            lezer = csv.DictReader(myCSVFile, delimiter=',')
            lijst = []
            aantalRegels = 0
            for regel in lezer:
                aantalRegels += 1
                omgezet = terugomzettenASCII(regel['uhjlvwudwlhqxpphu'])
                lijst.append(omgezet)
            if registratienummer in lijst:
                print('Deze kluizen zijn in gebruik:', infoPubliek())
                print('Kies een kluis van 1 t/m 99 die niet bezet is.')
                invoer = input('Welk kluisnummer wilt u? ')
                while True:
                    if invoer in infoPubliek():
                        print('Deze stallingsplaats is al in gebruik.')
                        invoer = input('Welk kluisnummer wilt u? ')
                    elif len(invoer) > 2:
                        print('Het laatste stallingsnummer is 99.')
                        invoer = input('Welk kluisnummer wilt u? ')
                    else:
                        wachtwoordStallingsplaats = input('Voer een wachtwoord in voor uw stallingsplaats: ')
                        while ',' in wachtwoordStallingsplaats:
                            print('Uw wachtwoord mag geen komma bevatten.')
                            wachtwoordStallingsplaats = input('Voer een wachtwoord in voor uw stallingsplaats: ')

                        wachtwoord = omzettenASCII(wachtwoordStallingsplaats)
                        vandaag = datetime.datetime.today()
                        s = vandaag.strftime("%d-%b-%Y, %I:%M:%S")
                        datum = omzettenASCII(s)
                        invoer = omzettenASCII(invoer)
                        registratieNummer = omzettenASCII(registratienummer)
                        return invoer, wachtwoord, datum, registratieNummer

with open('stalling.csv', 'a', newline = '') as myCSVFile:
    schrijven = csv.writer(myCSVFile)
    schrijven.writerow(plekVrij())
