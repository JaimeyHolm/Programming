def toon_aantal_kluizen_vrij():
    infile = open('Bagagekluizen.txt', 'r')
    aantalregels = 12 - len(infile.readlines())
    infile.close()
    return aantalregels


def nieuwe_kluis():
    infile = open('Bagagekluizen.txt', 'r')



def kluis_openen():
    infile = open('Bagagekluizen.txt', 'r')
    invoer = infile.readlines()
    infile.close()

#def kluis_teruggeven():


print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geef mijn kluis terug')
optie = (int(input('Voer nummer van optie in: ')))

if optie == 1:
    print('Er zijn in totaal', toon_aantal_kluizen_vrij(), 'kluizen vrij!')


#elif optie == 2:



#elif optie == 3:



#elif optie == 4:



else:
    print ('\nDe opgegeven waarde is ongeldig.')
    optie = (int(input('Voer nummer van optie in: ')))