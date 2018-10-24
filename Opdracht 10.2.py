import random
def monopolyworp():
    i = 1
    while True:
        dobbelsteen1 = random.randrange(1,7)
        dobbelsteen2 = random.randrange(1,7)

        if dobbelsteen1 == dobbelsteen2 and i == 3:
            print(dobbelsteen1, '+', dobbelsteen2, '(Direct naar de gevangenis)')
            break

        elif dobbelsteen1 == dobbelsteen2:
            print(dobbelsteen1, '+', dobbelsteen2, '=', dobbelsteen1 + dobbelsteen2, '(Dubbel)')

        else:
            print(dobbelsteen1, '+', dobbelsteen2, '=', dobbelsteen1 + dobbelsteen2)
            break

        i += 1

print (monopolyworp())