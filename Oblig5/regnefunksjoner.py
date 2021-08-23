def addisjon(a,b):
    return a + b

def subtraksjon(a,b):
    return (a) - (b)

def divisjon(a,b):
    return (a) / (b)

assert subtraksjon(20,5) == 15
assert subtraksjon(-20,-5) == -15
assert subtraksjon(20,-5) == 25

assert divisjon(10,5) == 2
assert divisjon(-10,-5) == 2
assert divisjon(10,-5) == -2

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

def skrivBeregninger():
    a, b = input('Skriv inn i to tall: ').split(',')
    a, b = [float(a), float(b)]
    sum = addisjon(a, b)
    sub = subtraksjon(a, b)
    div = divisjon(a, b)
    print(f'Resultat av summering: {sum}')
    print(f'Resultat av subtraksjon: {sub}')
    print(f'Resultat av divisjon: {div}')

    tommer = float(input('Skriv inn antall tommer: '))
    cm = tommerTilCm(tommer)
    print(f'Resultat: {cm}')


skrivBeregninger()