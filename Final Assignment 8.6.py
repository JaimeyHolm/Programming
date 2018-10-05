def toon_aantal_kluizen_vrij():
    infile = open('Bagagekluizen.txt', 'r')
    aantalregels = 12 - len(infile.readlines())
    infile.close()
    return aantalregels


def nieuwe_kluis():
    if toon_aantal_kluizen_vrij() > 0:
        kluizen = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        infile = open('Bagagekluizen.txt', 'r')
        for nummer in range(12 - toon_aantal_kluizen_vrij()):
            tmp = infile.read(2)
            if ';' in tmp:
                tmp = tmp.replace(';', '')
                kluizen.remove(tmp)

            else:
                kluizen.remove(tmp)
            infile.readline()
        print('De kluis die u krijgt is kluis', kluizen[0])
        code = input('Voer een code in voor uw kluis: ')
        infile = open('Bagagekluizen.txt', 'a')
        infile.write(kluizen[0]+';'+code+'\n')
        infile.close()
        return kluizen[0]

    else:
        return ('Geen kluizen vrij')

    infile.close


def kluis_openen(kluisnummer, code):
    infile = open('Bagagekluizen.txt', 'r')
    kluizen = []
    for kluis in range(12 - toon_aantal_kluizen_vrij()):
        tmp = infile.readline()
        tmp = tmp.replace('\n', '')
        tmp = tmp.split(';')
        if tmp[0] == kluisnummer:
            if tmp[1] == code:
                return ('Uw kluis is open.')
            else:
                return('Uw kluinummer en code komen niet overeen.')
        else:
            pass
    infile.close()


print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
optie = (int(input('Voer nummer van optie in: ')))
print('\n')

if optie == 1:
    print('Er zijn in totaal', toon_aantal_kluizen_vrij(), 'kluizen vrij!')

elif optie == 2:
    print('Kluis', nieuwe_kluis(), 'is van u.')

elif optie == 3:
    kluisnummer = input('Voer uw kluisnummer in: ')
    code = input('Voer uw code in: ')
    print(kluis_openen(kluisnummer, code))

else:
    print ('\nDe opgegeven waarde is ongeldig.')
    optie = (int(input('Voer nummer van optie in: ')))