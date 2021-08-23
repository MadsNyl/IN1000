print('Skriv inn en datoer med ett tall for dag og måned, i riktig rekkefølge. Format "måned" + "dag": 0525')
dato1 = input('Første dato: ')
dato2 = input('Andre dato: ')

dato1, dato2 = [int(dato1), int(dato2)]

if dato1 > dato2:
    print('Riktig rekkefølge!')
elif dato1 < dato2:
    print('Feil rekkefølge!')
elif dato1 == dato2:
    print('Samme dato!')