def sum():
    total = 0
    aantalKeer = 0
    while True:
        nextInt = (input('next int: '))

        if nextInt == '0':
            break


        else:
            total += int(nextInt)
            aantalKeer += 1

    return aantalKeer, total

x, y = sum()
print('Er zijn', x, 'getallen ingevoerd, de som is:', y)