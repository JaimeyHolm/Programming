bedrag = 4356

mensen = input('Hoeveel personen gaan mee op reis? ')

while True:
    if int(mensen) < 0:
        print('Negatieve getallen zijn niet toegestaan!')
        break

    try:
        print('Het bedrag per persoon is', bedrag/ int(mensen), 'euro!')
        break

    except ZeroDivisionError:
        print('Delen door 0 kan niet!')
        break

    except ValueError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
        break

    except:
        print('Onjuiste invoer!')
        break