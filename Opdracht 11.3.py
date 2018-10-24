import csv

with open('Opdracht 11.3.csv', 'r') as myCSVFile:
    invoer = csv.reader(myCSVFile, delimiter = ';')
    hoogsteScore = 0
    for regel in invoer:
        score = regel[2]
        score = int(score)
        if score > hoogsteScore:
            hoogsteScore = score
            datum = regel[1]
            naam = regel[0]
    print('De hoogste score is {}, wat behaald is op {} door {}.'.format(hoogsteScore,datum,naam))
