infile = open('Opdracht 7.2.txt')
invoer = infile.readlines()
infile.close()

for i in invoer:
    i.split(',')
    print(i[8:-1], 'heeft kaartnummer', i[:6])


