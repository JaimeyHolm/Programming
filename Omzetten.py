def omzettenASCII():
    invoer = input('Wat wil je omzetten? ')
    for c in invoer:
        cope = ord(c) - 3
        print(chr(cope), end='')

omzettenASCII()