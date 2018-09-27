import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %I:%M:%S")
ervoor = ' '
binnenkomer = input('Wat is je naam: ')

while binnenkomer != ervoor:
    invoer = open('Opdracht 7.4.txt', 'a')
    invoer.write(s, ' ', binnenkomer, '\n')
    invoer.close()
    binnenkomer = ervoor
    binnenkomer = input('Wat is je naam: ')