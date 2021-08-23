def antallBokstaver(ord):
    bokstaver = list(ord)
    print(len(bokstaver))

def antallOrd(setning):
    ordliste = setning.split()
    ordbok = dict((x, ordliste.count(x))) for x in set(ordliste)
    

antallOrd('hei jeg heter mads, og jeg er fra mads')