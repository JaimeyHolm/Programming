import xmltodict

def lezen(fileName):
    with open(fileName) as myXMLFile:
        inlezen = myXMLFile.read()
        lijst = xmltodict.parse(inlezen)
        return lijst


artikelen = lezen('Opdracht 13.1.xml')
artikelnaam = artikelen['artikelen']['artikel']

for artikel in artikelnaam:
    print(artikel['naam'])