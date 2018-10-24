def code(invoerstring):
    zin = invoerstring
    zin = list(zin)
    zinASCII = []
    for letter in range(len(zin)):
        ASCIInummerOrg = ord(zin[letter]) + 3
        ASCIIletter = chr(ASCIInummerOrg)
        zinASCII.append(ASCIIletter)
        print(zinASCII[letter], end='')
    print('')

invoer = input('Voer uw naam, uw vertrekstation en uw aankomststation in: ')
print(code(invoer))

