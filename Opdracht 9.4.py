def ticker():
    dict = {}
    with open("opdracht 9.4.txt") as f:
        for line in f:
            namen = line.replace('\n', '')
            namen = namen.split(':')
            dict[namen[0]] = namen[1]
    return dict

dict = ticker()
bedrijf = input('Enter Company Name: ')
print('Ticker Symbol: {} \n'.format(dict[bedrijf]))

afkorting = input('Enter Ticker Symbol: ')
for regel in dict:
    if dict[regel] == afkorting:
        print ('Campany Name = {}'.format(regel))