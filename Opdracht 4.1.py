cijferICOR = 5.5
cijferCSN = 6.0
cijferPROG = 6.5

gemiddelde = (cijferICOR + cijferCSN + cijferPROG/ 3)
punten = cijferICOR + cijferCSN + cijferPROG
beloning = punten * 30

overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'
print(overzicht)
