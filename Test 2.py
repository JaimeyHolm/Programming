import datetime

def tijd():
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%H")
    s = int(s)
    if s < 12:
        return('Goedemorgen')
    elif s >= 12 and s < 18:
        return('Goedemiddag')
    elif s > 18:
        return('Goedenavond')

print(tijd())