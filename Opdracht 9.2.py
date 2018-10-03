while True:
    string = (input('Geef een string van 4 letters: '))
    aantalLetters = len(string)

    if aantalLetters == 4:
        break

    else:
        print(string, 'heeft', aantalLetters, 'letters')

print('Inlezen van correcte string:', string, 'is geslaagd')