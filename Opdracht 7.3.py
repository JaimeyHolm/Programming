def aantalRegels():
    invoer = open ('Opdracht 7.2.txt', 'r')
    telRegels = invoer.readlines()
    invoer.close()
    return len(telRegels)


def grootsteGetal():
    invoer = open('opdracht 7.2.txt')
    getallenlijst = []
    n = 6
    i = 0
    while i < n:
        getallenlijst.append(invoer.read(6))
        invoer.readline()
        i += 1
    invoer.close()
    return max(getallenlijst)


print ('Deze file telt ', aantalRegels(), ' regels')

print ('Het grootste kaartnummer is: ' + grootsteGetal() + ' en dat staat op lijn 4')