# spør om brukeren vil ha en brus, gjør om til små bokstaver
# kjører programmet om igjen til ja eller nei har blitt svart
while True:

    svar = input('Hei, har du lyst på en brus? ').lower()


    if svar == 'ja':
        print('Her har du en brus!')
        break
    elif svar == 'nei':
        print('Den er grei.')
        break
    else:
        continue