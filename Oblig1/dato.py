# tar imot datoer i måneder og sjekker de opp mot hverandre for å finne riktig rekkefølge

print('Skriv inn en datoer med tall for dag og måned, i riktig rekkefølge.')
dag1, måned1 = input('Første dato: ').split(',')
dag2, måned2 = input('Andre dato: ').split(',')

# omgjør til heltall fra strenger
dag1, måned1, dag2, måned2 = [int(dag1), int(måned1), int(dag2), int(måned2)]

# sjekker rekkefølgen på inputen
if måned1 > måned2:
    print('Riktig rekkefølge!')
elif måned1 < måned2:
    print('Feil rekkefølge!')
elif måned1 == måned2:
    if dag1 > dag2:
        print('Riktig rekkefølge!')
    elif dag1 < dag2:
        print('Feil rekkefølge!')
    elif dag1 == dag2:
        print('Samme dato!')


