mineOrd = []

def slaaSammen(streng1, streng2):
    return streng1 + streng2

def skrivUt(liste):
    for el in liste:
        print(el)


kjørLøkke = True

while kjørLøkke:
    bruker_svar = input('Trykk "i" for å slå sammen to strenger,\nTrykk "u" for å skrive ut din liste,\nTrykk "s" for å avslutte programmet: ')
    if bruker_svar == 'i':
        streng1, streng2 = input('Skriv inn to strenger: ').split(',')
        sammenslått = slaaSammen(streng1, streng2)
        mineOrd.append(sammenslått)
    elif bruker_svar == 'u':
        skrivUt(mineOrd)
    elif bruker_svar == 's':
        kjørLøkke = False